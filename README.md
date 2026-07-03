
# Contract Risk Intelligence Platform

## Overview

The Contract Risk Intelligence Platform is an AI-powered legal document analysis solution built on Microsoft Azure. The platform uses Retrieval-Augmented Generation (RAG) to help legal professionals analyze contracts, identify potential risks, and receive grounded responses supported by source citations.

Instead of relying solely on general AI model knowledge, the solution retrieves relevant contract language from Azure AI Search and uses GPT-5-mini to generate responses based on actual document content.

***

## Business Problem

Legal teams often spend significant time:

* Reviewing large collections of contracts
* Identifying risk exposure
* Locating specific clauses
* Comparing terms across agreements

Manual review can be time-consuming and difficult to scale.

***

## Solution

The Contract Risk Intelligence Platform allows users to ask natural-language questions about contracts and receive AI-generated analysis with supporting citations.

### Example Questions

```text
Which contracts contain automatic renewal clauses?

Which agreements allow termination without cause?

Which contracts expose the client to unlimited liability?

What confidentiality obligations survive termination?
```

***

## Architecture

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
Contract Risk Analysis
      ↓
Filename-Based Citations
      ↓
Power Apps
```

***

## Technology Stack

### Azure

* Azure AI Foundry
* Azure AI Search
* Azure Blob Storage
* Azure Functions

### AI Models

* GPT-5-mini
* text-embedding-3-small

### Development

* Python
* OpenAI SDK
* Azure Search SDK
* REST APIs

### Power Platform

* Power Apps
* Power Automate

***

## Key Features

✅ Retrieval-Augmented Generation (RAG)

✅ Vector Search

✅ Semantic Search

✅ GPT-Powered Contract Analysis

✅ Filename-Based Citations

✅ Azure Function API

✅ Power Apps Interface

✅ Production Azure Deployment

***

## Citation Enhancement

The platform was enhanced to improve transparency and legal traceability.

Previous citation format:

```text
[Source 1]
[Source 2]
```

Current citation format:

```text
NDA-001.pdf

Vendor-Agreement-001.pdf

Employment-Agreement-001.pdf
```

This allows attorneys to immediately identify supporting source documents.

***

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
├── function_app.py
├── host.json
├── requirements.txt
└── README.md
```

***

## Project Status

### Version 1.0

✅ Azure Infrastructure

✅ Azure AI Search

✅ Contract Indexing

✅ Python RAG Application

✅ Azure Function Deployment

✅ Power Automate Integration

✅ Power Apps Integration

✅ Citation Enhancement

✅ End-to-End Testing

✅ Production Deployment

***

## Future Enhancements

### Phase 6

* Law Firm Demo Website
* Contract Upload Portal
* Automated Contract Ingestion
* Expanded Risk Analysis Framework

***

## Final Outcome

Successfully designed, developed, and deployed an end-to-end Azure-based AI solution that performs contract risk analysis using Retrieval-Augmented Generation, Azure AI Search, GPT-5-mini, and filename-based citations.

🚀 **Status: Deployed and Operational**

***




