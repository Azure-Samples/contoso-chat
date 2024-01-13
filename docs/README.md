# Let's Build Contoso Chat

!!!example "About This Guide"

    This developer guide teaches you how to build, run, evaluate, deploy, and use, an LLM application with Retrieval Augmented Generation. We'll walk you through the end-to-end development process from _prompt engineering_ to _LLM Ops_ with step-by-step instructions all the way. Here's what you need to know:
    
     - We'll build **[Contoso Chat](https://github.com/Azure-Samples/contoso-chat)**, a customer service AI application for the **[Contoso Outdoors](https://github.com/Azure-Samples/contoso-web)** company website. 
     - We'll use **[Azure AI Studio](https://ai.azure.com)** and **[Prompt Flow](https://github.com/microsoft/promptflow)** to streamline  LLMOps from ideation to operationalization!

## What You'll Need

The main workshop takes about **60-75 minutes** to complete. Significant time is taken by _provisioning_ Azure resources and _deploying_ your final promptflow-based LLM application. Some parts of the workshop **may be automated or completed in parallel** to reduce that time.

You will need:

 - A _GitHub account_ (with GitHub Codespaces access)
 - An _Azure account_ (with Azure OpenAI access)
 - A _modern browser_ (to run Codespaces, access Azure portals)
 - Familiarity with _Python, Jupyter Notebooks & VS Code_

!!!example "Instructor Led Sessions"

    This documentation is meant for self-guided completion of the workshop. The workshop may also be offered in _instructor-led sessions_ at events like the [2024 Microsoft AI Tour](https://aka.ms/msaitour) using a _Lab On Demand_ platform that comes with a pre-provisioned Azure subscription and built-in guide. Instructions should be comparable, but experience may vary.

## What You'll Build

The main workshop focuses on building **Contoso Chat**, an AI application that uses Retrieval Augmented Generation to build a _customer support_ chat agent for **Contoso Outdoors**, an online store for outdoor adventurers. The end goal is to _integrate customer chat support_ into the website application for Contoso Outdoors, as shown below.
       
![Multi-turn Contoso Chat](./img/scenario/07-customer-multiturn-conversation.png)

!!!example "Azure-Samples Repositories"

    The workshop will refer to two different applications in the overview. The _[contoso-chat](https://github.com/Azure-Samples/contoso-chat)_ sample provides the basis for building our **RAG-based LLM Application** to implement the chat-completion AI. The  _[contoso-web](https://github.com/Azure-Samples/contoso-web)_ implements the **Contoso Outdoors Web Application** with an integrated chat interface that website visitors will use, to interact with our deployed AI application. We'll cover the details in the **[01 | Introduction](./01%20|%20%20Introduction/index.md)** section of the guide.

## How You'll Build It

The workshop is broadly organized into these steps, some of which may run in parallel.

- [x] Setup Development Environment (GitHub Codespaces)
- [x] Provision Project Resources (Azure Portal, Azure AI Studio)
- [x] Configure Environment (Local & Cloud Connections)
- [x] Configure Cloud Environment (Prompt Flow Connections)
- [x] Run, Evaluate & Push Prompt Flow (Local, VS Code)
- [x] Run, Deploy & Test Prompt Flow (Cloud, Azure AI Studio)

This completes the _ideating_ and _building_ phases of the LLM Application Lifecycle, and begins the _operationalization_ phase for real-world usage. 

![LLM Lifecycle Stage Flows](./img/concepts/03-llm-stage-flows.png)

If time permits, complete these additional steps that showcase capabilities in that final phase.

- [x] Integrate with Deployed Endpoint (Contoso Web)
- [x] Explore Responsible AI Usage (Contoso Chat)
- [x] Automate Deployments (GitHub Actions)
- [x] Explore Intents (Context-based Agent Routing)

!!!example "Breakout Session: End-to-End App Development: Prompt Engineering to LLM Ops"

    This workshop is inspired by (and extended from) the demo shown in this breakout session from Microsoft Ignite 2023. Watch the recording to understand the **significance of the LLM Ops terminology** and get an early introduction to new tooling we'll use in this session.

    <iframe width="1000" height="420" src="https://www.youtube.com/embed/DdOylyrTOWg" title="End-to-End AI App Development: Prompt Engineering to LLMOps | BRK203"></iframe>

## Start Workshop 🚀

Ready to get started building this application? Pick your starting point from the two options below - and #LetsGo 

- Want to understand the application before you start? 👉🏽 Go to **[01 | Introduction](./01%20|%20%20Introduction/index.md)**.
- Want to jump straight into building the application? 👉🏽 Go to **[02 | Workshop](./02%20|%20Workshop/00-hello-learner.md)** section. 