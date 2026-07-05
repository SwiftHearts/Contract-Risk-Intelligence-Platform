
# Solution Architecture

## Overview

The Contract Risk Intelligence Platform supports two deployment models:

1. **Enterprise Law Firm Deployment** – built with Microsoft Power Platform for legal teams operating within Microsoft 365.
2. **Public Demonstration Deployment** – built with Streamlit to allow website visitors, recruiters, and prospective clients to experience the solution without requiring Microsoft authentication.

Both front ends use the same Azure-based Retrieval-Augmented Generation (RAG) backend to provide grounded contract analysis and source-cited responses.

***

# Enterprise Law Firm Architecture

This deployment model demonstrates how the solution would typically be implemented within a law firm using Microsoft technologies.

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

## Purpose

The enterprise version provides attorneys and legal professionals with a secure, user-friendly experience inside the Microsoft ecosystem.

Users interact with a Power Apps interface while Power Automate orchestrates communication with an Azure Function API that performs Retrieval-Augmented Generation (RAG) using Azure AI Search and GPT-5-mini.

## Business Value

✅ Microsoft 365 Integration

✅ Low-Code User Experience

✅ Secure Internal Deployment

✅ Familiar Interface for Legal Teams

✅ Scalable Enterprise Architecture

✅ Rapid Workflow Automation

***

# Public Demonstration Architecture

This deployment model demonstrates the public-facing version of the platform used for portfolio demonstrations, recruiter evaluation, website visitors, and prospective client engagements.

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

## Purpose

The public version allows anyone to experience the platform without requiring a Microsoft account.

The Streamlit application provides a lightweight web interface while leveraging the same Azure-based backend used by the enterprise deployment.

## Business Value

✅ No Sign-In Required

✅ Public Demonstration Environment

✅ Recruiter and Portfolio Review

✅ Client Proof-of-Concept

✅ Rapid AI Application Deployment

✅ Easy Website Integration

***

# Shared Retrieval-Augmented Generation (RAG) Backend

Both deployment models use the same Azure AI architecture.

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

***

# Core Components

## Contract Repository

### Azure Blob Storage

Stores contract PDF documents used for indexing and retrieval.

### Sample Documents

```text
Employment-Agreement-001.pdf
NDA-001.pdf
SaaS-Agreement-001.pdf
Service-Agreement-001.pdf
Vendor-Agreement-001.pdf
Vendor-Agreement-002.pdf
```

***

## Azure AI Search

Provides semantic retrieval and vector search capabilities across indexed contract content.

### Responsibilities

* Contract chunk storage
* Metadata storage
* Vector storage
* Semantic search
* Similarity search
* Content retrieval

### Indexed Fields

```text
chunk_id
parent_id
chunk
title
text_vector
```

***

## Embedding Model

### text-embedding-3-small

Used to generate vector embeddings for:

* Contract content
* User questions

### Embedding Dimensions

```text
1536
```

***

## Azure Function API

Acts as the application layer between user interfaces and Azure AI services.

### Responsibilities

* Receive user questions
* Generate embeddings
* Execute vector search
* Retrieve relevant contract content
* Create retrieval context
* Invoke GPT-5-mini
* Return answers and citations

***

## Azure AI Foundry

Provides the AI models that power contract analysis.

### Model Deployments

✅ GPT-5-mini

✅ text-embedding-3-small

### Responsibilities

* Embedding generation
* Contract reasoning
* Risk analysis
* Grounded response generation

***

## GPT-5-mini

Generates answers based only on retrieved contract content supplied by the RAG pipeline.

### Capabilities

✅ Risk Identification

✅ Contract Analysis

✅ Clause Comparison

✅ Grounded Responses

✅ Citation-Based Explanations

***

## Filename-Based Citations

Responses include citations referencing actual contract documents.

### Example

```text
NDA-001.pdf

Vendor-Agreement-001.pdf

Employment-Agreement-001.pdf
```

### Benefits

✅ Improved Transparency

✅ Better Traceability

✅ Reduced Hallucination Risk

✅ Increased User Trust

✅ Faster Legal Review

***

# End-to-End Workflow

1. User submits a contract-related question.
2. The question is converted into a vector embedding using text-embedding-3-small.
3. Azure AI Search performs vector similarity search.
4. Relevant contract chunks are retrieved.
5. Azure Function assembles retrieval context.
6. GPT-5-mini generates a grounded response.
7. Supporting filenames are returned as citations.
8. Results are displayed in Power Apps or Streamlit.

***

# Deployment Models Summary

| Component        | Enterprise Deployment | Public Deployment                                 |
| ---------------- | --------------------- | ------------------------------------------------- |
| Front End        | Power Apps            | Streamlit                                         |
| Workflow Layer   | Power Automate        | Direct API Call                                   |
| API Layer        | Azure Function API    | Azure Function API                                |
| Search Layer     | Azure AI Search       | Azure AI Search                                   |
| AI Layer         | Azure AI Foundry      | Azure AI Foundry                                  |
| LLM              | GPT-5-mini            | GPT-5-mini                                        |
| Authentication   | Microsoft 365         | Public Access                                     |
| Primary Audience | Law Firms             | Recruiters, Website Visitors, Prospective Clients |

***

# Architecture Outcome

The Contract Risk Intelligence Platform demonstrates two real-world deployment approaches built on a shared Azure AI backend:

* An enterprise-ready Microsoft 365 solution using Power Apps and Power Automate for legal professionals.
* A publicly accessible Streamlit application for demonstrations, portfolio presentation, and client evaluation.

Both deployments use Retrieval-Augmented Generation (RAG), Azure AI Search, Azure AI Foundry, GPT-5-mini, Azure Functions, and filename-based citations to provide transparent, grounded contract risk analysis.
