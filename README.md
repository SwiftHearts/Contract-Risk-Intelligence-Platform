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
