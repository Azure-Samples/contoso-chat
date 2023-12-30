# End to End LLM App development with Azure AI Studio and Prompt Flow

This tutorial provides step-by-step guidance for a hands-on workshop that can take learners through the end-to-end development process for _Contoso Chat_, an LLM-based customer support application that allows users to chat with an AI to learn more abou the Contoso Trek product catalog. This tutorial can be used for self-guided learning or instructor-led sessions and _prioritizes using GitHub Codespaces_ with a pre-configured development environment, for convenience. 

**Pre-Requisites**:
 - An Azure Subscription → [Create one for free if needed.](https://azure.microsoft.com/free/cognitive-services)
 - Subscription enabled for Azure OpenAI access → [Apply here to enable it.](https://aka.ms/oai/access)
 - Access permissions to deploy models in Azure OpenAI → [Learn more about access roles](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control) 
 - Model availability (quota, region) → [Required: `gpt-3.5-turbo`, `gpt-4`, `text-embedding-ada-002`](https://learn.microsoft.com/azure/ai-services/openai/concepts/models)
 - Azure AI Search with Semantic Search enabled → [Requires paid Standard Tier with feature enabled](https://learn.microsoft.com/azure/search/semantic-how-to-enable-disable?tabs=enable-portal)

> [!IMPORTANT]
> Learners who participate in an instructor-led workshop session that uses the [Skillable LabOnDemand](https://labondemand.com) platform will be given a pre-provisioned Azure subscription for that session. Self-guided learners (at home) will need to bring their own.

---

## 1. 👋🏽 | Introduction

### 1.1 What is LLM Ops?

### 1.2 LLMOps App Lifecycle

### 1.3 Retrieval Augmented Generation

### 1.4 LLM Evaluation Metrics

## 2. 💬 | Lab Outline

### 2.1 Application

### 2.2 Pre-Requisites

### 2.3 Learning Objectives

## 3. 👩🏽‍💻 | Lab Environment

### 4.1 Dev Container

### 4.2 Visual Studio Code

### 4.3 Azure CLI

## 5. 🤖 | Azure AI Platform

### 5.1 Azure Portal

### 5.2 Azure AI Studio

### 5.3 Azure ML Studio

### 5.4 Prompt Flow Extension

### 5.5 Prompt Flow CLI

## 6. ⚙️ | Setup AI Project

### 6.1 Create Azure AI Resource

### 6.2 Create OpenAI Deployments (models)

### 6.3 Create Azure AI Project

### 6.4 Update `config.json`

### 6.5 Create Azure AI Search

### 6.6 Populate Search Index (products)

### 6.7 Create Azure Cosmos DB

### 6.8 Populate NoSQL Database (customers)

### 6.9 Update `.env`

### 6.10 Create cloud Connections

### 6.11 Create local Connections

### 6.12 Review Azure AI Setup

## 7. ⛓ | Build Prompt Flow

### 7.1 Explore `contoso_chat` components

### 7.2 Understand `contoso_chat` prompt flow

### 7.3 Run `contoso_chat` prompt flow

## 8. 🧾 | Evaluate Prompt Flow

### 8.1 Explore `eval` components

### 8.2 Understand `eval` prompt flow

### 8.3 Run `multi-eval` prompt flow 

### 8.4 Run `eval` prompt flows in VS Code

### 8.5 View `eval` results on Azure

## 9. ⬆️  | Deploy Prompt FLow

### 9.1 Push `contoso_chat` prompt flow to Azure

### 9.2 Deploy `contoso_chat` to Azure endpoint

### 9.3 Test `contoso_chat` deployment

## 10. 🥳 | Recap & Next Steps

### 10.1 What did we do?

### 10.2 What did we learn?

### 10.3 How can you go further?

## 11. 🧰 | Troubleshooting & Tips

### 11.1 Connection issues

### 11.2 Dependency issues

### 11.3 Runtime issues

### 11.4 Azure AI Search issues

### 11.5 Azure AI Studio issues
