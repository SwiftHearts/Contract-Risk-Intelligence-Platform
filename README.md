# Contract Risk Intelligence Platform

## Overview

The Contract Risk Intelligence Platform is an AI-powered legal document analysis solution built on Microsoft Azure. The platform uses Retrieval-Augmented Generation (RAG) to help legal professionals analyze contracts, identify potential risks, and receive grounded responses supported by source citations.

Instead of relying solely on general AI model knowledge, the solution retrieves relevant contract language from Azure AI Search and uses GPT-5-mini to generate responses based on actual contract content.

The project demonstrates two deployment models:

- Enterprise law firm implementation using Power Apps and Power Automate
- Public web application using Streamlit

Both versions share the same Azure-based RAG backend.

---

## Live Demo

Try the public version of the application:

### Public Streamlit Demo

https://contract-risk-intelligence-platform-a4rlq2uwlfqhaahjj9dpdr.streamlit.app/

### Features

- AI-powered contract risk analysis
- Retrieval-Augmented Generation (RAG)
- Azure AI Search vector retrieval
- GPT-5-mini analysis
- Filename-based source citations

No Microsoft sign-in required.

---

## Business Problem

Legal teams often spend significant time:

- Reviewing large collections of contracts
- Identifying risk exposure
- Locating specific clauses
- Comparing terms across agreements

Manual review can be time-consuming and difficult to scale.

---

## Solution

The Contract Risk Intelligence Platform allows users to ask natural-language questions about contracts and receive AI-generated analysis with supporting citations.

### Example Questions

```text
Which contracts contain automatic renewal clauses?

Which agreements allow termination without cause?

Which contracts expose the client to unlimited liability?

What confidentiality obligations survive termination?
```

---

## Architecture

### Enterprise Law Firm Deployment

This architecture demonstrates how the solution would typically be implemented within a law firm using Microsoft 365 and the Power Platform.

```text
Attorney / Legal Team
          ↓
Power Apps
          ↓
Power Automate
          ↓
Azure Function API
          ↓
Azure AI Search
          ↓
Azure AI Foundry
          ↓
GPT-5-mini
          ↓
Contract Risk Analysis
          ↓
Filename-Based Citations
          ↓
Power Apps
```

### Public Demonstration Deployment

This architecture demonstrates the publicly accessible version used for portfolio demonstrations, recruiter evaluations, and prospective client engagements.

```text
Website Visitor
          ↓
Streamlit App
          ↓
Azure Function API
          ↓
Azure AI Search
          ↓
Azure AI Foundry
          ↓
GPT-5-mini
          ↓
Contract Risk Analysis
          ↓
Filename-Based Citations
          ↓
Streamlit App
```

### Shared RAG Backend

Both deployment models utilize the same Azure AI architecture.

```text
Contract PDFs
      ↓
Azure Blob Storage
      ↓
Azure AI Search Index
      ↓
Vector Embeddings
(text-embedding-3-small)
      ↓
Vector Search
      ↓
Azure Function API
      ↓
Azure AI Foundry
      ↓
GPT-5-mini
      ↓
Contract Risk Analysis
      ↓
Filename-Based Citations
```

---

## Solution Screenshots

### Public Streamlit Demo

Screenshots/01-streamlit-demo.png

The public Streamlit application allows users to perform AI-powered contract risk analysis without requiring Microsoft authentication.

---

### Azure AI Model Deployments

Screenshots/02-model-deployments.png

GPT-5-mini and text-embedding-3-small are deployed within Azure AI Foundry to provide contract reasoning and vector embedding generation.

---

### Power Automate Integration

Screenshots/03-power-automate-flow.png

Power Automate orchestrates communication between Power Apps and the Azure Function API, enabling secure and scalable contract analysis workflows.

---

### Power Apps Contract Risk Analysis

Screenshots/04-power-app-question-analysis.png

Legal professionals can ask natural-language questions and receive AI-generated risk analysis grounded in contract content retrieved through Azure AI Search.

---

### Citation Transparency

Screenshots/05-power-app-citations.png

Responses include filename-based citations that improve traceability, transparency, and legal review workflows.

Example citation output:

```text
Vendor-Agreement-001.pdf

SaaS-Agreement-001.pdf

Employment-Agreement-001.pdf
```

---

### Azure AI Search Vector Index

Screenshots/06-vector-search-fields.png

Contract chunks, metadata, and embeddings are stored in Azure AI Search to support semantic retrieval and Retrieval-Augmented Generation (RAG).

---

## Technology Stack

### Azure

- Azure AI Foundry
- Azure AI Search
- Azure Blob Storage
- Azure Functions

### AI Models

- GPT-5-mini
- text-embedding-3-small

### Development

- Python
- OpenAI SDK
- Azure Search SDK
- REST APIs

### Front End

- Streamlit
- Power Apps

### Workflow Automation

- Power Automate

---

## Key Features

✅ Retrieval-Augmented Generation (RAG)

✅ Vector Search

✅ Semantic Search

✅ GPT-Powered Contract Analysis

✅ Filename-Based Citations

✅ Azure Function API

✅ Public Streamlit Demo

✅ Power Apps Enterprise Interface

✅ Azure AI Foundry Integration

✅ Production Azure Deployment

✅ Public Website Demonstration

---

## Citation Enhancement

The platform was enhanced to improve transparency and legal traceability.

### Previous Citation Format

```text
[Source 1]

[Source 2]
```

### Enhanced Citation Format

```text
NDA-001.pdf

Vendor-Agreement-001.pdf

Employment-Agreement-001.pdf
```

This enhancement allows legal professionals to immediately identify supporting source documents and validate AI-generated responses more efficiently.

---

## Repository Structure

```text
Contract-Risk-Intelligence-Platform
│
├── Docs
│   └── architecture-notes.md
│
├── Src
│   └── contract_risk_app.py
│
├── Screenshots
│   ├── 01-streamlit-demo.png
│   ├── 02-model-deployments.png
│   ├── 03-power-automate-flow.png
│   ├── 04-power-app-question-analysis.png
│   ├── 05-power-app-citations.png
│   └── 06-vector-search-fields.png
│
├── function_app.py
├── host.json
├── requirements.txt
└── README.md
```

---

## Project Status

### Version 1.0 - Publicly Deployed

✅ Azure Infrastructure

✅ Azure AI Search

✅ Contract Indexing

✅ Python RAG Application

✅ Azure Function API Deployment

✅ Azure AI Foundry Integration

✅ GPT-5-mini Contract Analysis

✅ Source-Cited Responses

✅ Power Automate Integration

✅ Power Apps Integration

✅ Public Streamlit Deployment

✅ Public Website Demonstration

✅ End-to-End Testing

✅ Production Deployment

---

## Future Enhancements

### Phase 2

- Contract Upload Portal
- Automated Contract Ingestion
- Expanded Risk Analysis Framework
- User Authentication and Roles
- Additional Contract Templates

---

## Final Outcome

Successfully designed, developed, secured, and deployed an end-to-end Azure AI solution for legal contract analysis.

The platform combines Azure AI Search, Azure AI Foundry, GPT-5-mini, Azure Functions, Streamlit, Power Apps, and Power Automate to provide grounded contract risk analysis with filename-based citations.

The solution demonstrates two deployment models:

- An enterprise Microsoft 365 implementation using Power Apps and Power Automate for legal professionals.
- A public Streamlit application for website visitors, recruiters, and prospective clients.

### Technologies Demonstrated

- Azure AI Foundry
- Azure AI Search
- Vector Search
- Retrieval-Augmented Generation (RAG)
- GPT-5-mini
- text-embedding-3-small
- Azure Functions
- Streamlit
- Power Automate
- Power Apps
- Python
- REST APIs

🚀 **Status: Publicly Deployed and Operational**

✅ Live Demo Available

✅ No Sign-In Required

✅ Portfolio Ready

✅ Website Ready