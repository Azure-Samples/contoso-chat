# Workshop Overview

**This is a hands-on workshop to teach you how to build a RAG-based LLM application _end-to-end_ using Azure AI Studio and Prompt Flow.**

This lab has been designed to work in both instructor-led sessions (at a Microsoft event) and as a self-guided exercise (at home). _The instructions below are meant for self-guided learning_. Instructor-led sessions will have their own adapted version of this manual, using the [Skillable LabOnDemand](https://skillable.com) platform and come with a built-in Azure subscription.


!!! info "PRE-REQUISITES"

    - **GitHub Account** - with GitHub Codespaces. _Free quota is sufficient_.
    - **Your own laptop** - fully-charged. _This is a 75-minute lab_.
    - **Modern browser** - on laptop. _To launch the Lab-on-Demand session_.
    - **Azure subscription** - with Azure OpenAI access. _For model deployments_.


## Learning Objectives

In this lab we'll learn to _build, run, evaluate, and deploy_ a RAG-based application ("Contoso Chat") using Azure AI Studio and Prompt Flow. By the end of this lab, you should be able to:

1. Explain **LLMOps** concepts & benefits.
1. Explain **Prompt Flow** concept & benefits.
1. Explain **Azure AI Studio** features & usage.
1. Use **Prompt Flow** on Visual Studio Code
1. Design **RAG-based LLM Applications**
1. Build, run, evaluate & deploy RAG-based LLM apps **on Azure**.

## Dev Environment

This repository is instrumented with a [dev container](https://containers.dev) that gives you a pre-configured development environment with minimal effort required on your part. To get started, launch the dev container using GitHub Codespaces (cloud) or Docker Desktop (local device).

## Related Resources

You'll use the following resources in this lab:

- [Contoso Chat](https://github.com/Azure-Samples/contoso-chat) - as the RAG-based AI app _we will build_.
- [Contoso Outdoors](https://github.com/Azure-Samples/contoso-web) - as the web-based app _using our AI_.
- [Github Codespaces](https://github.com/codespaces) - as the dev container _we will launch_
- [Visual Studio Code](https://code.visualstudio.com/) - as the default editor _we will work in_
- [Azure Portal](https://portal.azure.com) - for managing our Azure subscription.
- [Azure AI Studio (Preview)](https://ai.azure.com) - for managing Azure AI resources.
- [Azure ML Studio](https://ml.azure.com) - for some AI project configuration.
- [Prompt Flow](https://github.com/microsoft/promptflow) - for streamlining end-to-end LLM app dev