# Contoso-Chat: Hands-on Workshop

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&machine=basicLinux32gb&repo=725257907&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=UsEast)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/contoso-chat)

---

## About Contoso Chat

The Contoso Chat repository provides a reference sample for an Azure AI Architecture and workflow to build a custom RAG-based copilot **code-first** on Azure AI Studio. The sample has been actively used to skill up developers in core Azure AI tools, services, and practices, since its creation in 2023.

**The current version (v3) of the sample follows this architecture**.

![](./../img/arch-contoso-retail-aca.png)

## Workshop Versions

The Contoso Chat sample has been used to run hands-on workshops for different internal and external developer audiences. This table tracks the versions for historical reference, identifying the key capabilities that were in focus at the time.


> | Version | Description | Technologies |
> |:---|:---|:---|
> | [v0](https://github.com/Azure-Samples/contoso-chat/tree/cc2e808eee29768093866cf77a16e8867adbaa9c) | #MSAITour Nov 2023 (Skillable) | Prompt flow (DAG), Jnja (template), Provisioning (scripts) |
> | [v1](https://github.com/Azure-Samples/contoso-chat/tree/msbuild-lab322) | #MSBuild May 2024 Lab322 (Skillable) | Prompt flow (DAG), Jnja (template), Provisioning (scripts) |
> | [v2](https://github.com/Azure-Samples/contoso-chat/tree/raghack-24) | #RAGHack 2024 (Self-Guided) | Prompt flow (Flex), Prompty (template), Provisioning (AZD), Hosting (AIP) | 
> | [v3](https://github.com/Azure-Samples/contoso-chat/tree/raghack-24)  🆕| MSAITour 2024-25 (prompty asset, ACA)- Skillable + AZD | Prompty (template), Python (runtime), Provisioning (AZD), Hosting (ACA) | 
> | [main](https://github.com/Azure-Samples/contoso-chat/tree/raghack-24) | Version that will be in active development (RAG, GenAIOps) | Provisioning Ideation - Evaluation - Deployment - Monitoring - CI/CD | 
> | | |

This folder contains the content for the Contoso-Chat workshop. It is written in Markdown using the [mkdocs Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/?h=ad) extensions. 

You can read this content with any Markdown viewer (for example, Visual Studio Code or GitHub). Start here: [Build a Retail Copilot Code-First on Azure AI](docs/index.md).

For the best experience build the documentation and view it in a browser window using the instructions below.

## Workshop Guide

The current repository is instrumented with a `docs/workshop/` folder that contains the step-by-step lab guide for developers, covering the entire workflow from resource provisioning to ideation, evaluation, deployment, and usage.

The workshop is designed to be used in two modes:
 - Instructor led workshops (e.g., #MSAITour, #MSIgnite)
 - Self-guided workshop (individually, at home)

You can view [a hosted version of the workshop guide](https://aka.ms/aitour/contoso-chat/workshop) on the Azure AI Tour website for quick reference. You can also **preview and extend** the workshop directly from this source:

1. Install the `mkdocs-material` package
    ```bash
    pip install mkdocs-material
    ```

2. Run the `mkdocs serve` command from the `workshop` folder
    ```bash
    cd docs/workshop
    mkdocs serve -a localhost:5000
    ```
This should open the dev server with a preview of the workshop guide on the specified local address. Simply open a browser and navigate to `http://localhost:5000` to view the content.


**Note:** If you are currently viewing the repo from GitHub Codespaces or a Docker Desktop hosted _dev container_ launched from this repo, then you should already have the `mkdocs-material` package installed - and can go directly to step 2.
