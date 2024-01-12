# About Contoso Chat

!!!example "Workshop: Build a RAG-based LLM App with Azure AI Studio and Prompt Flow"

    Want to learn how to build, evaluate, and deploy, an LLM application using Retrieval Augemented Generation? This guide walks you step-by-step through the end-to-end development process _from prompt engineering to LLM Ops_. 
    
     - We'll build **[Contoso Chat](https://github.com/Azure-Samples/contoso-chat)**, a customer service AI application for the **[Contoso Outdoors](https://github.com/Azure-Samples/contoso-web)** company website. 
     - We'll use **[Azure AI Studio](https://ai.azure.com)** and **[Prompt Flow](https://github.com/microsoft/promptflow)** to streamline  LLMOps from ideation to operationalization!

## Pre-Requisites

The core workshop should take you **60-75 minutes** to complete, from provisioning the Azure AI project to deploying and using your promptflow-based LLM application. You will need:

 - A GitHub account (with GitHub Codespaces access)
 - An Azure account (with Azure OpenAI access)
 - A modern browser (to run Codespaces, access Azure portals)

_Note:_ Instructor-led sessions may use a _LabOnDemand_ platform with a built-in Azure subscription. You will still need your own GitHub login with access to GitHub Codespaces. Personal accounts get a generous free quota for Codespaces that is sufficient for this lab.

## Workshop Outline

The workshop is broadly organized into these steps, some of which may run in parallel.

- [x] Setup Development Environment (GitHub Codespaces)
- [x] Provision Project Resources (Azure Portal, Azure AI Studio)
- [x] Configure Environment (Local & Cloud Connections)
- [x] Configure Cloud Environment (Prompt Flow Connections)
- [x] Run, Evaluate & Push Prompt Flow (Local, VS Code)
- [x] Run, Deploy & Test Prompt Flow (Cloud, Azure AI Studio)

If time and interest permit, extend your workshop exploration with these additional steps:

- [x] Integrate with Deployed Endpoint (Contoso Web)
- [x] Explore Responsible AI Usage (Contoso Chat)
- [x] Automate Deployments (GitHub Actions)
- [x] Explore Intents (Context-based Agent Routing)

!!!tip "Congratulations! You just shipped a Customer Support AI"

    If you successfully integrated the deployed endpoint with the Contoso Web application, your user experience should resemblet the screenshot below. Customers visit the site and browse product pages. The customer can now "chat" with the customer support AI (e.g., to ask questions about products or past orders) - using natural language, just as they would with a human customer support service agent.
    
![](./img/scenario/07-customer-multiturn-conversation.png)

!!!example "Ready to start building?" 

    **Head to the [Workshop](./02%20|%20Workshop/00-hello-learner.md) section!** of this site to see the Table of Contents, and start at the Lab Overview!

## Breakout Session

Want to get a better understanding of what **LLM Ops** means, or learn more about the tools and technologies covered today? Watch this recording of the breakout session from MS Ignite 2023, featuring the Contoso Chat demo that inspired this workshop.

<iframe width="1243" height="699" src="https://www.youtube.com/embed/DdOylyrTOWg" title="End-to-End AI App Development: Prompt Engineering to LLMOps | BRK203"></iframe>
