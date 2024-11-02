# Before You Begin


!!! task "MAKE YOUR CHOICE NOW: WHICH WORKSHOP GUIDE DO YOU WANT?"

    === "Self-Guided"

        - [ ] Requires you to use **your Azure subscription** (see pre-requisites)
        - [ ] Requires you to **self-provision the infrastructure** (see setup steps)
        - [ ] You will use your own laptop for this lab (make sure it's charged!)
        - [X] No time constraints - work at your own pace.

    === "Microsoft AI Tour"

        - [X] Uses the **Skillable** platform with **built-in Azure subscription** 
        - [X] Has **pre-provisioned** Azure resources for a fast start (dedicated resource group)
        - [ ] You will use your own laptop for this lab (make sure it's charged!)
        - [ ] Session is 75 mins. Assume you have 1 hour to complete the lab.


    === "Microsoft Ignite"

        - [X] Uses the **Skillable** platform with **built-in Azure subscription** 
        - [X] Has **pre-provisioned** Azure resources for a fast start (dedicated resource group)
        - [X] You will use the workstation provided to learners in-venue, for this lab.
        - [ ] Session is 75 mins. Assume you have 1 hour to complete the lab.


## Learning Goals

This hands-on workshop teaches you how to **build, evaluate, and deploy a retail copilot** code-first on Azure AI, with step-by-step instructions that take you from prompt to production.

- Our solution use the [Retrieval Augmented Generation (RAG) pattern](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation) to ground chat AI responses in the retailer's product catalog and cusomer data.
- Our implementation uses [Prompty](https://prompty.ai) for ideation, [Azure AI Studio](https://ai.azure.com) as the platform for code-first copilot development, and [Azure Container Apps](https://aka.ms/azcontainerapps) for hosting the deployed copilot.
- Our development environment uses [Dev Containers](https://containers.dev) to give you a pre-built workspace in the cloud (with GitHub Codespaces) or on device (with Docker Desktop) with minimal effort.
- Our codebase is structured as an `azd-template`, using the [Azure Developer CLI](https://aka.ms/azd) to provision infrastructure and deploy the solution, with a single command (`azd up`).

The [Introduction](./01-Introduction/01-App-Scenario.md) section will dive into more details on what we'll build, and how!


## Learning Options

This guide is setup for use in both self-guided (at home) and instructor-led (in-venue) sessions, as shown in the tabs at the top of this page. Self-guided sessions can be completed at any time. Instructor-led options are currently available **to registered attendees** at the following events:

- [Microsoft AI Tour (2024-2025)](https://aka.ms/aitour) 
- [Microsoft Ignite 2024](https://ignite.microsoft.com/en-US/sessions?search=LAB401)

**Make sure you set the tab to the right session for you!**. The choice will be enforced site-wide.

## Learning Resources

1. **Prompty** | [Documentation](https://prompty.ai) · [Specification](https://github.com/microsoft/prompty/blob/main/Prompty.yaml)  · [Tooling](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty) · [SDK](https://pypi.org/project/prompty/)
1. **Azure AI Studio**  | [Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)  · [Architecture](https://learn.microsoft.com/azure/ai-studio/concepts/architecture) · [SDKs](https://learn.microsoft.com/azure/ai-studio/how-to/develop/sdk-overview) ·  [Evaluation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app)
1. **Azure AI Search** | [Documentation](https://learn.microsoft.com/azure/search/)  · [Semantic Ranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 
1. **Azure Container Apps**  | [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)  · [Deploy from code](https://learn.microsoft.com/en-us/azure/container-apps/quickstart-repo-to-cloud?tabs=bash%2Ccsharp&pivots=with-dockerfile)
1. **Responsible AI**  | [Overview](https://www.microsoft.com/ai/responsible-ai)  · [With AI Services](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext)  · [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/)
