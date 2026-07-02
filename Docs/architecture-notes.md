

# Architecture Notes

## Project Overview

**Project Name:** Contract Risk Intelligence Platform

**Purpose:**
An AI-powered legal document analysis solution that uses Retrieval-Augmented Generation (RAG) to identify and explain potential risks in contracts using Azure AI Search and GPT-5-mini.

**Status:** ✅ Version 1.0 Complete

***

# Architecture

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
Python Application
      ↓
GPT-5-mini
      ↓
Contract Risk Analysis
      ↓
Source Citations
```

***

# Azure Resources

## Resource Group

**Name:** `rg-sterling-legal`

**Region:** Central US

**Status:** ✅ Created

**Purpose:**
Central container for all Azure resources used by the project.

***

## Azure AI Foundry

**Project:** `contract-risk-intelligence`

**Status:** ✅ Created

**Purpose:**
Hosts AI models and supports prompt execution for the RAG application.

### Deployments

✅ gpt-5-mini

✅ text-embedding-3-small

**Deployment Type:** Global Standard

***

## Azure AI Search

**Name:** `sterling-contract-search`

**Tier:** Free

**Region:** Central US

**Status:** ✅ Created

**Purpose:**
Indexes contract content and provides vector-based retrieval for the RAG workflow.

***

## Azure Storage Account

**Name:** `sterlinglegalstorage`

**Region:** Central US

**Performance:** Standard

**Redundancy:** LRS

**Status:** ✅ Created

**Purpose:**
Stores source contract documents used by Azure AI Search.

***

## Blob Container

**Name:** `contracts`

**Access Level:** Private

**Status:** ✅ Created

**Purpose:**
Stores contract PDF files for indexing and retrieval.

***

# Contract Dataset

## Storage Location

```text
contracts/
```

## Documents

* Employment-Agreement-001.pdf
* NDA-001.pdf
* SaaS-Agreement-001.pdf
* Service-Agreement-001.pdf
* Vendor-Agreement-001.pdf
* Vendor-Agreement-002.pdf

**Status:** ✅ Uploaded

**Purpose:**
Provides sample legal agreements containing intentionally varied contract language for testing RAG retrieval and risk analysis.

***

# Risk Framework

**Location:** `Docs/risk-framework.md`

**Status:** ✅ Created

**Purpose:**
Defines legal risk categories evaluated by the application.

Examples include:

* Termination Risk
* Liability Risk
* Indemnification Risk
* Auto-Renewal Risk
* Payment Risk
* Compliance Risk

***

# Azure AI Search Index

## Index Name

```text
rag-1782927108192
```

## Fields

| Field        | Purpose                                      |
| ------------ | -------------------------------------------- |
| chunk\_id    | Unique chunk identifier                      |
| parent\_id   | Parent document identifier                   |
| chunk        | Human-readable contract text                 |
| title        | Contract title                               |
| text\_vector | Vector embedding used for semantic retrieval |

### Embedding Dimension

```text
1536
```

Generated using:

```text
text-embedding-3-small
```

***

# Phase 1 – Contract Ingestion

## Objective

Ingest contract documents into Azure AI Search and create a searchable vector index.

## Results

✅ Documents Indexed: 6

✅ Vector Index Created

✅ Embeddings Generated

✅ Semantic Search Enabled

## Technologies Used

* Azure AI Foundry
* Azure AI Search
* Azure Blob Storage
* GPT-5-mini
* text-embedding-3-small

## Outcome

Contract content was successfully indexed and made available for semantic and vector retrieval.

***

# Phase 2 – Python Application Integration

## Objective

Connect a custom Python application to Azure AI Search and GPT-5-mini.

## Environment

### Python

```text
Python 3.14.3
```

### Installed Packages

```text
openai
azure-search-documents
python-dotenv
```

### Configuration

Environment variables managed through:

```text
.env
```

***

# Validation Results

## Retrieval Validation

Successfully connected Python to Azure AI Search.

Validated:

✅ Search endpoint access

✅ API key authentication

✅ Search index connectivity

✅ Document retrieval

### Retrieved Fields

* chunk\_id
* parent\_id
* chunk
* title
* text\_vector

### Result

Successfully retrieved indexed contract content from Azure AI Search.

***

## Generation Validation

Successfully connected Python to GPT-5-mini hosted in Azure AI Foundry.

Validated:

✅ Endpoint connectivity

✅ API authentication

✅ GPT-5-mini deployment access

✅ Chat completion generation

### Result

GPT-5-mini successfully generated responses from Python.

***

# Phase 2 Milestone – First End-to-End RAG Application

## Objective

Combine retrieval and generation into a complete contract analysis workflow.

## Workflow

1. User submits a contract-related question.
2. Application generates a vector embedding of the question.
3. Azure AI Search performs vector similarity search.
4. Relevant contract chunks are retrieved.
5. Retrieved content is assembled into a citation-aware prompt.
6. GPT-5-mini generates a contract risk analysis.
7. Sources are cited using retrieved document chunks.

***

## Example Questions

* Which contracts contain auto-renewal clauses?
* Which contracts have termination risks?
* Which contracts contain indemnification language?
* Which contracts have unfavorable liability terms?
* Summarize the top risks in this contract.

***

## Outcome

✅ Retrieval working

✅ Generation working

✅ Citations working

✅ End-to-end RAG workflow working

The application successfully returned contract risk assessments with source-backed citations, demonstrating a complete Retrieval-Augmented Generation architecture for legal document analysis.

***

# Lessons Learned

Key lessons from this project include:

* Vector embeddings represent semantic meaning rather than individual words.
* Effective RAG systems require both retrieval quality and prompt quality.
* Azure AI Search can serve as a scalable retrieval layer for AI applications.
* Embedding models and chat models play distinct roles in a RAG architecture.
* Infrastructure planning, service quotas, and model availability are important considerations when building cloud-based AI solutions.

***

# Project Status

## Contract Risk Intelligence Platform v1.0

**Status:** ✅ Complete

### Technology Stack

* Azure AI Foundry
* Azure AI Search
* Azure Blob Storage
* GPT-5-mini
* text-embedding-3-small
* Python
* OpenAI SDK
* Azure Search SDK

### Capabilities

✅ Contract Retrieval

✅ Vector Search

✅ GPT-Powered Analysis

✅ Source Citations

✅ End-to-End RAG Workflow

### Final Outcome

Successfully built an end-to-end Azure-based Retrieval-Augmented Generation application that analyzes legal contracts and produces source-backed contract risk assessments. 🚀

***

# Phase 4 – Integration Architecture

## Goal

Connect the Power Apps front end to the Azure AI backend to provide real-time contract risk analysis with source citations.

## Planned Architecture

Power Apps
    ↓
Power Automate
    ↓
Azure Function (Python)
    ↓
Azure AI Search
    ↓
GPT-5-mini
    ↓
JSON Response
    ↓
Power Apps

## Data Flow

1. User enters a contract question in Power Apps.
2. Power Automate receives the question.
3. Power Automate sends the question to an Azure Function.
4. Azure Function performs vector retrieval from Azure AI Search.
5. Retrieved contract chunks are sent to GPT-5-mini.
6. GPT-5-mini generates a risk assessment.
7. Azure Function returns:
   - Answer
   - Source citations
8. Power Apps displays the response.
