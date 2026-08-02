# Import Streamlit and requests libraries for building the web interface and making HTTP requests
import streamlit as st

# Import the requests library for making HTTP requests to the Azure Function
import requests

# Define the URL of the Azure Function that handles contract risk analysis requests
FUNCTION_URL = "https://sterling-contract-risk-api-dve9a8gcbzbwczgt.eastus2-01.azurewebsites.net/api/ContractRiskAnalysis"

# Set the page configuration for the Streamlit app, including the title and layout
st.set_page_config(
    page_title="Contract Risk Intelligence Platform",
    layout="wide"
)

# Set the title and description of the Streamlit app, providing context for users
st.title("Contract Risk Intelligence Platform")

# Set a brief description of the app's purpose, emphasizing its AI-powered capabilities for analyzing legal agreements
st.write(
    "Analyze legal agreements using AI-powered contract risk intelligence."
)

# Display an informational message to users, clarifying that the demonstration uses sample contracts and does not constitute legal advice
st.info(
    "This demonstration uses sample contracts and is for informational purposes only. It does not constitute legal advice."
)

# Create a text area for users to input their contract risk questions, with a placeholder example provided
question = st.text_area(
    "Contract Risk Question",
    placeholder="Please enter your legal contract risk question. Example: What termination risks exist in this agreement?"
)

# Create a button that users can click to initiate the contract risk analysis process
if st.button("Analyze Contract"):

    # Check if the user has entered a question
    if question:

        # Display a spinner to indicate that the analysis is in progress while the request is being processed
        with st.spinner("Analyzing contract..."):

            # Make a POST request to the Azure Function with the user's question as JSON data
            response = requests.post(
                FUNCTION_URL,
                json={
                    "question": question
                }
            )

            result = response.json()

            
    # Check if the analysis was successful; if so, display the answer and sources in the Streamlit app        
    if result.get("status") == "success":

        # Display the analysis results in the Streamlit app, including the answer and sources used for the analysis
        st.subheader("Analysis")
        st.markdown(result.get("answer", ""))

        # Display the sources used for the analysis in a subheader section, listing each source as a markdown bullet point
        st.subheader("Sources Used")

        # Loop through the sources provided in the result and display each source as a markdown bullet point in the Streamlit app
        for source in result.get("sources", []):
            st.markdown(f"- {source}")

    else:
        st.error(result.get("message", "An unknown error occurred."))

# Add a divider and a caption to provide additional context about the app's development and the technologies used
st.divider()

st.caption(
    "Built by Swift Hearts AI using Azure AI Search, Azure AI Foundry, GPT-5-mini, Azure Functions, and Retrieval-Augmented Generation (RAG)."
)