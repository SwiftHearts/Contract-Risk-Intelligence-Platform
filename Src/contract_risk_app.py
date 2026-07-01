import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

from openai import AzureOpenAI


# ------------------------------------------------------------
# Load environment variables from .env
# ------------------------------------------------------------

load_dotenv()


# ------------------------------------------------------------
# Azure AI Search settings
# ------------------------------------------------------------

SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("SEARCH_KEY")
SEARCH_INDEX_NAME = os.getenv("SEARCH_INDEX_NAME")


# ------------------------------------------------------------
# Azure AI Foundry / GPT settings
# ------------------------------------------------------------

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

GPT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
EMBEDDING_DEPLOYMENT_NAME = os.getenv(
    "AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"
)


# ------------------------------------------------------------
# Create clients
# ------------------------------------------------------------

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=SEARCH_INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_KEY)
)

openai_client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)


# ------------------------------------------------------------
# Step 1: Create embedding for the user's question
# ------------------------------------------------------------

def create_question_embedding(question):
    embedding_response = openai_client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT_NAME,
        input=question
    )

    return embedding_response.data[0].embedding


# ------------------------------------------------------------
# Step 2: Retrieve relevant contract chunks from Azure AI Search
# ------------------------------------------------------------

def retrieve_contract_chunks(question, top_k=5):
    question_embedding = create_question_embedding(question)

    vector_query = VectorizedQuery(
        vector=question_embedding,
        k_nearest_neighbors=top_k,
        fields="text_vector"
    )

    results = search_client.search(
        search_text=question,
        vector_queries=[vector_query],
        select=["chunk_id", "parent_id", "chunk", "title"],
        top=top_k
    )

    retrieved_chunks = []

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

def build_context(chunks):
    context_parts = []

    for index, item in enumerate(chunks, start=1):
        title = item.get("title") or "Unknown contract"
        chunk_id = item.get("chunk_id") or "Unknown chunk"
        chunk_text = item.get("chunk") or ""

        context_parts.append(
            f"[Source {index}]\n"
            f"Title: {title}\n"
            f"Chunk ID: {chunk_id}\n"
            f"Text:\n{chunk_text}\n"
        )

    return "\n---\n".join(context_parts)


# ------------------------------------------------------------
# Step 4: Ask GPT-5-mini to analyze contract risk
# ------------------------------------------------------------

def analyze_contract_risk(question, chunks):
    context = build_context(chunks)

    system_message = """
You are a contract risk intelligence assistant for a fictitious law firm called Sterling Legal Partners.

Your job is to analyze contract language and identify potential legal, business, operational, and compliance risks.

Use only the provided contract excerpts as your source material.

If the provided excerpts do not contain enough information to answer the question, say so clearly.

When you make a claim, cite the relevant source using this format:
[Source 1], [Source 2], etc.

Structure your answer with:
1. Short Answer
2. Key Contract Evidence
3. Risk Analysis
4. Recommended Next Steps
5. Sources Used
"""

    user_message = f"""
User question:
{question}

Retrieved contract excerpts:
{context}
"""

    response = openai_client.chat.completions.create(
        model=GPT_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
    )

    return response.choices[0].message.content


# ------------------------------------------------------------
# Step 5: Full app flow
# ------------------------------------------------------------

def run_contract_risk_app():
    print("\nContract Risk Intelligence Platform")
    print("-----------------------------------")

    question = input("\nAsk a contract risk question: ")

    print("\nRetrieving relevant contract chunks...\n")
    chunks = retrieve_contract_chunks(question)

    if not chunks:
        print("No relevant contract chunks were found.")
        return

    print("Retrieved sources:")
    for index, chunk in enumerate(chunks, start=1):
        print(f"[Source {index}] {chunk.get('title')} | Chunk ID: {chunk.get('chunk_id')}")

    print("\nGenerating contract risk analysis...\n")
    answer = analyze_contract_risk(question, chunks)

    print("\nContract Risk Analysis")
    print("----------------------")
    print(answer)


# ------------------------------------------------------------
# Run the app
# ------------------------------------------------------------

if __name__ == "__main__":
    run_contract_risk_app()