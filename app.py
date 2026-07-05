import streamlit as st
import requests

FUNCTION_URL = "https://sterling-contract-risk-api-dve9a8gcbzbwczgt.eastus2-01.azurewebsites.net/api/ContractRiskAnalysis"

st.set_page_config(
    page_title="Contract Risk Intelligence Platform",
    layout="wide"
)

st.title("Contract Risk Intelligence Platform")

st.write(
    "Analyze legal agreements using AI-powered contract risk intelligence."
)

st.info(
    "This demonstration uses sample contracts and is for informational purposes only. It does not constitute legal advice."
)

question = st.text_area(
    "Contract Risk Question",
    placeholder="Please enter your legal contract risk question. Example: What termination risks exist in this agreement?"
)

if st.button("Analyze Contract"):

    if question:

        with st.spinner("Analyzing contract..."):

            response = requests.post(
                FUNCTION_URL,
                json={
                    "question": question
                }
            )

            result = response.json()

            st.subheader("Analysis")
            st.markdown(result["answer"])

            st.subheader("Sources Used")

            for source in result["sources"]:
                st.markdown(f"- {source}")

st.divider()

st.caption(
    "Built by Swift Hearts AI using Azure AI Search, Azure AI Foundry, GPT-5-mini, Azure Functions, and Retrieval-Augmented Generation (RAG)."
)