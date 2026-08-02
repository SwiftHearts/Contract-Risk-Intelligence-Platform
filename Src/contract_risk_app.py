# Import os to access environment variables
import os

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Import AzureKeyCredential to authenticate with Azure services
from azure.core.credentials import AzureKeyCredential

# Import SearchClient to interact with Azure AI Search
from azure.search.documents import SearchClient

# Import VectorizedQuery to perform vector-based searches
from azure.search.documents.models import VectorizedQuery

# Import AzureOpenAI to interact with Azure OpenAI services
from openai import AzureOpenAI


# ------------------------------------------------------------
# Load environment variables from .env
# ------------------------------------------------------------

# Load environment variables from a .env file into the application's environment, 
# allowing access to sensitive information such as API keys and endpoints
load_dotenv()


# ------------------------------------------------------------
# Azure AI Search settings
# ------------------------------------------------------------

# Define the Azure AI Search endpoint, key, and index name from environment variables

# Get the Azure AI Search endpoint from the environment variable SEARCH_ENDPOINT
SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
# Get the Azure AI Search key from the environment variable SEARCH_KEY
SEARCH_KEY = os.getenv("SEARCH_KEY")
# Get the Azure AI Search index name from the environment variable SEARCH_INDEX_NAME
SEARCH_INDEX_NAME = os.getenv("SEARCH_INDEX_NAME")


# ------------------------------------------------------------
# Azure AI Foundry / GPT settings
# ------------------------------------------------------------

# Define Azure OpenAI settings from environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Define the deployment names for GPT and embeddings from environment variables
GPT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
EMBEDDING_DEPLOYMENT_NAME = os.getenv(
    "AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"
)


# ------------------------------------------------------------
# Create clients
# ------------------------------------------------------------

# Create a SearchClient from Azure SDK to interact with Azure AI Search
# The SearchClient is initialized with the endpoint, index name, and credential 
# (AzureKeyCredential) to authenticate requests to the Azure AI Search service.
search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=SEARCH_INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_KEY)
)

# Create an AzureOpenAI client to interact with Azure OpenAI services
openai_client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)


# ------------------------------------------------------------
# Step 1: Create embedding for the user's question
# ------------------------------------------------------------

# Create an embedding for the user's question using the specified embedding model
def create_question_embedding(question):
    # Call the Azure OpenAI API to create an embedding for the user's question
    embedding_response = openai_client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT_NAME,
        input=question
    )

    # Return the embedding vector from the response
    return embedding_response.data[0].embedding


# ------------------------------------------------------------
# Step 2: Retrieve relevant contract chunks from Azure AI Search
# ------------------------------------------------------------

# Retrieve relevant contract chunks from Azure AI Search based on the user's question
def retrieve_contract_chunks(question, top_k=5):
    question_embedding = create_question_embedding(question)

    # Create a vector query to find the top K nearest neighbors based on the question embedding
    vector_query = VectorizedQuery(
        vector=question_embedding,
        # Specify the number of top results to retrieve (5 by default)
        k_nearest_neighbors=top_k,
        # Specify the field in the index that contains the vector embeddings
        fields="text_vector"
    )

    # Perform the search using the vector query and retrieve relevant fields
    results = search_client.search(
        # Use the user's question as the search text to find relevant contract chunks
        # Both the search text and vector query are used to find relevant documents in the index
        search_text=question,
        # Do a semantic search by using the vector query to find the top K nearest 
        # neighbors based on the question embedding
        # Return the results in a python list
        vector_queries=[vector_query],
        # Specify the fields to retrieve from the search results, including 
        # chunk ID, parent ID, chunk text, and title
        select=["chunk_id", "parent_id", "chunk", "title"],
        # Specify the number of top results to retrieve (5 by default)
        top=top_k
    )

    # Process the search results and extract relevant information into a list of dictionaries
    retrieved_chunks = []

    # Loop through the search results and extract relevant information for each chunk
    for result in results:
        retrieved_chunks.append({
            "chunk_id": result.get("chunk_id"),
            "parent_id": result.get("parent_id"),
            "title": result.get("title"),
            "chunk": result.get("chunk"),
            "score": result.get("@search.score")
        })

    return retrieved_chunks


# ------------------------------------------------------------
# Step 3: Build context with citation labels
# ------------------------------------------------------------

# Build context for GPT-5-mini with citation labels based on the retrieved contract chunks
def build_context(chunks):
    # Initialize an empty list to hold the context parts for GPT-5-mini
    context_parts = []

    # Add each chunk to the context with citation labels
    # Return both the index and the item in the enumerate function 
    # to keep track of the chunk number, beginning the index at 1 for user-friendly numbering
    for index, item in enumerate(chunks, start=1):
        # Extract the title, chunk ID, and chunk text from each item in the dictionary, 
        # providing default values if they are None
        title = item.get("title") or "Unknown contract"
        # Extract the chunk ID and chunk text from each item in the dictionary, 
        # providing default values if they are None
        chunk_id = item.get("chunk_id") or "Unknown chunk"
        # Extract the chunk text from each item in the dictionary, providing a default value if it is None
        chunk_text = item.get("chunk") or ""

        # Add the chunk to the context with a citation label
        # This will enable the returned string to be formatted with the document title, 
        # chunk ID, and chunk text for GPT-5-mini to reference in its analysis
        context_parts.append(
            f"DOCUMENT: {title}\n"
            f"Chunk ID: {chunk_id}\n"
            f"Text:\n{chunk_text}\n"
)
    # Join all context parts with a separator and return the final context string
    return "\n---\n".join(context_parts)


# ------------------------------------------------------------
# Step 4: Ask GPT-5-mini to analyze contract risk
# ------------------------------------------------------------

# Analyze contract risk using GPT-5-mini based on the user's question and the retrieved contract chunks
def analyze_contract_risk(question, chunks):
    # Build context with citation labels for GPT-5-mini
    context = build_context(chunks)

    # Define the system message to instruct GPT-5-mini on how to analyze contract risk
    system_message = """
You are a contract risk intelligence assistant for a fictitious law firm called Sterling Legal Partners.

Your job is to analyze contract language and identify potential legal, business, operational, and compliance risks.

Use only the provided contract excerpts as your source material.

If the provided excerpts do not contain enough information to answer the question, say so clearly.

When you make a claim:

- Cite the actual document filename.
- Never use Source 1, Source 2, or similar labels.
- Only cite filenames that appear in the provided context.

Example:

(Employment-Agreement-001.pdf)

or

Sources Used:
- Employment-Agreement-001.pdf
- Vendor-Agreement-001.pdf

Structure your answer with:
1. Short Answer
2. Key Contract Evidence
3. Risk Analysis
4. Recommended Next Steps
5. Sources Used
"""

    # Define the user message to provide GPT-5-mini with the user's question and the retrieved contract excerpts
    user_message = f"""
User question:
{question}

Retrieved contract excerpts:
{context}
"""
    # Call the Azure OpenAI API to generate a response from GPT-5-mini based on the system and user messages
    response = openai_client.chat.completions.create(
        model=GPT_DEPLOYMENT_NAME,
        messages=[
            # Provide the system message to instruct GPT-5-mini on how to analyze contract risk
            {"role": "system", "content": system_message},
            # Provide the user message to give GPT-5-mini the user's question and the retrieved contract excerpts
            {"role": "user", "content": user_message}
        ],
    )

    # Return the content of the first message in the response, which contains GPT-5-mini's analysis of the contract risk
    return response.choices[0].message.content


# -----------------------------------------------------------
# Azure Function helper
# ------------------------------------------------------------

# Run the contract risk analysis and return the answer and sources used
def run_contract_risk_analysis(question):
    chunks = retrieve_contract_chunks(question)

    if not chunks:
        return {
            "answer": "No relevant contract chunks were found.",
            "sources": []
        }

    # Analyze the contract risk using GPT-5-mini based on the user's question and the retrieved contract chunks
    answer = analyze_contract_risk(question, chunks)

    # Ensure that the human-readable answer is returned along with the sources used for the analysis
    sources = []
    
    for chunk in chunks:
        # Extract the title from each chunk
        title = chunk.get("title")

        # If the title is not None and not already in the sources list, add it
        if title and title not in sources:
            sources.append(title)

    return {
        "answer": answer,
        "sources": sources
    }

# ------------------------------------------------------------
# Step 5: Full app flow
# ------------------------------------------------------------

# Run the contract risk analysis app in a command-line interface
def run_contract_risk_app():
    print("\nContract Risk Intelligence Platform")
    print("-----------------------------------")

    question = input("\nAsk a contract risk question: ")

    print("\nRetrieving relevant contract chunks...\n")
    chunks = retrieve_contract_chunks(question)

    if not chunks:
        print("No relevant contract chunks were found.")
        return

    # Print the retrieved sources for the user's reference
    print("Retrieved sources:")
    for index, chunk in enumerate(chunks, start=1):
        print(f"[Source {index}] {chunk.get('title')} | Chunk ID: {chunk.get('chunk_id')}")

    # Print the retrieved contract chunks for the user's reference
    print("\nGenerating contract risk analysis...\n")
    answer = analyze_contract_risk(question, chunks)

    # Print the final answer from GPT-5-mini for the user's reference
    print("\nContract Risk Analysis")
    print("----------------------")
    print(answer)

    


# ------------------------------------------------------------
# Run the app
# ------------------------------------------------------------

# If this script is run directly, execute the run_contract_risk_app function to start 
# the command-line interface for contract risk analysis.
if __name__ == "__main__":
    run_contract_risk_app()