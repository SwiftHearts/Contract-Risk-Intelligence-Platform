

# Contract Risk Intelligence Platform

## Project Overview

### Project Name

**Contract Risk Intelligence Platform**

### Status

✅ **Version 1.0 – Deployed and Operational**

### Purpose

The Contract Risk Intelligence Platform is an AI-powered legal document analysis solution built on Microsoft Azure. The platform uses Retrieval-Augmented Generation (RAG) to analyze contracts, identify potential risks, and generate grounded responses supported by source citations.

Rather than relying solely on model knowledge, the application retrieves relevant contract content from Azure AI Search and uses GPT-5-mini to generate responses based on actual contract language.

### Business Problem

Legal professionals often spend significant time reviewing contracts, locating clauses, assessing risk, and comparing language across multiple agreements.

The Contract Risk Intelligence Platform streamlines this process by allowing attorneys and legal teams to ask natural-language questions and receive AI-generated analyses with direct references to supporting contract documents.

***

# Solution Architecture

## End-to-End Architecture

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
Azure Function
      ↓
GPT-5-mini
      ↓
Contract Risk Analysis
      ↓
Filename-Based Citations
      ↓
Power Apps
```

## User Experience Architecture

```text
Power Apps
      ↓
Power Automate
      ↓
Azure Function
      ↓
Azure AI Search
      ↓
GPT-5-mini
      ↓
Answer + Citations
      ↓
Power Apps
```

***

# Azure Resources

## Resource Group

**Name:** `rg-sterling-legal`

**Region:** Central US

**Status:** ✅ Active

### Purpose

Central container for all Azure resources used by the solution.

***

## Azure AI Foundry

**Project:** `contract-risk-intelligence`

**Status:** ✅ Active

### Purpose

Hosts the AI models used for embedding generation and response generation.

### Model Deployments

✅ gpt-5-mini

✅ text-embedding-3-small

**Deployment Type:** Global Standard

***

## Azure AI Search

**Name:** `sterling-contract-search`

**Region:** Central US

**Tier:** Free

**Status:** ✅ Active

### Purpose

Provides vector-based retrieval and semantic search across contract documents.

***

## Azure Storage Account

**Name:** `sterlinglegalstorage`

**Region:** Central US

**Redundancy:** LRS

**Performance Tier:** Standard

**Status:** ✅ Active

### Purpose

Stores contract PDF files for indexing and retrieval.

***

## Blob Container

**Name:** `contracts`

**Access Level:** Private

**Status:** ✅ Active

### Purpose

Stores source legal agreements used by the platform.

***

## Azure Function App

**Name:** `sterling-contract-risk-api`

**Status:** ✅ Deployed

### Purpose

Acts as the application API layer.

Responsibilities include:

* Receiving user questions
* Generating embeddings
* Executing vector search
* Building retrieval context
* Calling GPT-5-mini
* Returning analysis and citations

***

# Contract Dataset

## Storage Location

```text
contracts/
```

## Sample Documents

* Employment-Agreement-001.pdf
* NDA-001.pdf
* SaaS-Agreement-001.pdf
* Service-Agreement-001.pdf
* Vendor-Agreement-001.pdf
* Vendor-Agreement-002.pdf

**Status:** ✅ Indexed

### Purpose

Provides a representative collection of legal agreements containing various contractual obligations, risks, and clause structures used for testing retrieval and analysis capabilities.

***

# Risk Analysis Framework

**Location:** `Docs/risk-framework.md`

**Status:** ✅ Complete

### Purpose

Defines the contract risk categories evaluated by the application.

### Risk Categories

* Termination Risk
* Liability Risk
* Indemnification Risk
* Auto-Renewal Risk
* Payment Risk
* Compliance Risk

***

# Azure AI Search Configuration

## Search Index

```text
rag-1782927108192
```

### Indexed Fields

| Field        | Purpose                    |
| ------------ | -------------------------- |
| chunk\_id    | Unique chunk identifier    |
| parent\_id   | Parent document identifier |
| chunk        | Contract text chunk        |
| title        | Source document title      |
| text\_vector | Vector embedding           |

### Embedding Model

```text
text-embedding-3-small
```

### Embedding Dimensions

```text
1536
```

***

# Phase 1 – Contract Ingestion and Search Indexing

## Objective

Create a searchable vector index from a collection of legal contract documents.

## Technologies

* Azure Blob Storage
* Azure AI Search
* Azure AI Foundry
* text-embedding-3-small

## Results

✅ Contract PDFs uploaded

✅ Embeddings generated

✅ Vector index created

✅ Semantic search enabled

✅ Documents successfully indexed

## Outcome

Contract content became searchable through vector similarity and semantic retrieval techniques.

***

# Phase 2 – Python RAG Application

## Objective

Build a Retrieval-Augmented Generation pipeline using Azure AI Search and GPT-5-mini.

## Development Environment

### Python Version

```text
Python 3.14.3
```

### Key Packages

```text
openai
azure-search-documents
python-dotenv
```

### Configuration Management

```text
.env
```

***

## Retrieval Validation

Successfully validated:

✅ Search endpoint access

✅ Authentication

✅ Index connectivity

✅ Document retrieval

### Retrieved Fields

* chunk\_id
* parent\_id
* chunk
* title
* text\_vector

***

## Generation Validation

Successfully validated:

✅ GPT-5-mini deployment access

✅ Endpoint connectivity

✅ Authentication

✅ Chat completions

***

## End-to-End RAG Workflow

### Workflow

1. User submits a contract question.
2. An embedding is generated for the question.
3. Azure AI Search performs vector similarity search.
4. Relevant contract chunks are retrieved.
5. Context is assembled for GPT-5-mini.
6. GPT-5-mini generates analysis.
7. Supporting citations are returned.

### Example Questions

* Which contracts contain automatic renewal clauses?
* Which agreements allow termination without cause?
* Which contracts expose the client to unlimited liability?
* What confidentiality obligations survive termination?

### Outcome

✅ Retrieval working

✅ Generation working

✅ Source citations working

✅ Complete RAG workflow operational

***

# Phase 3 – Power Apps Prototype

## Objective

Provide a user-friendly front-end experience for contract analysis.

## Technologies

* Power Apps
* Power Automate

## Results

✅ User interface created

✅ Question submission implemented

✅ API integration completed

✅ Responses displayed within Power Apps

## Outcome

Users can perform contract analysis without interacting directly with Azure services.

***

# Phase 4 – Azure Function API Integration

## Objective

Create a scalable API layer between Power Platform and the RAG backend.

## Components

* Azure Function (Python)
* Azure AI Search
* Azure OpenAI
* Power Automate

## Results

✅ Function created

✅ API endpoint exposed

✅ Retrieval pipeline integrated

✅ Response formatting implemented

✅ Power Apps connectivity validated

## Outcome

A reusable API architecture was established for future web and application integrations.

***

# Phase 5 – Deployment and Citation Enhancement

## Phase 5A – Azure Deployment

### Objective

Deploy the application to Azure and validate production functionality.

### Results

✅ Azure CLI configured

✅ Azure authentication completed

✅ Azure Function deployed

✅ Production endpoint operational

✅ End-to-end testing completed

### Outcome

The Contract Risk Intelligence Platform became fully cloud-hosted and accessible through a production API.

***

## Phase 5B – Citation Enhancement

### Problem

The original citation strategy used generic references:

```text
[Source 1]
[Source 2]
[Source 3]
```

Although technically functional, these citations did not clearly identify supporting contract documents.

### Solution

The retrieval context was updated to include actual document filenames.

Example:

```text
DOCUMENT: NDA-001.pdf
```

GPT-5-mini was instructed to:

* Cite actual filenames
* Avoid generic source labels
* Reference only retrieved documents

### Result

Responses now include citations such as:

```text
NDA-001.pdf

Vendor-Agreement-001.pdf

Employment-Agreement-001.pdf
```

rather than abstract source identifiers.

### Business Value

✅ Improved citation transparency

✅ Better source traceability

✅ Increased attorney confidence

✅ Reduced review effort

✅ Reduced hallucination risk

***

# Lessons Learned

Key lessons from this project include:

* Effective RAG systems depend on retrieval quality as much as model quality.
* Vector embeddings capture semantic meaning rather than exact keyword matches.
* Grounded AI systems improve reliability and reduce hallucination risk.
* Azure AI Search provides an effective retrieval layer for enterprise AI applications.
* Clear citation strategies improve transparency, trustworthiness, and user adoption.

***

# Technology Stack

## Azure

* Azure AI Foundry
* Azure AI Search
* Azure Blob Storage
* Azure Functions

## AI Models

* GPT-5-mini
* text-embedding-3-small

## Development

* Python
* OpenAI SDK
* Azure Search SDK
* REST APIs

## Power Platform

* Power Apps
* Power Automate

***

# Production Capabilities

✅ Contract Retrieval

✅ Vector Search

✅ Semantic Search

✅ GPT-Powered Contract Analysis

✅ Source Traceability

✅ Filename-Based Citations

✅ Power Apps Integration

✅ Azure Deployment

✅ End-to-End RAG Workflow

***

# Final Outcome

The Contract Risk Intelligence Platform demonstrates a complete Azure-based Retrieval-Augmented Generation architecture for legal document analysis.

The solution retrieves relevant contract language from Azure AI Search, generates grounded responses using GPT-5-mini, and provides filename-based citations that improve transparency and traceability for legal review.

**Status:** 🚀 Deployed, Operational, and Successfully Validated End-to-End.
