# Build a Retail Copilot Code-First on Azure AI

This instructions are for participants of the Workshop "Build a Retail Copilot Code-First on Azure AI" at Microsoft AI Tour 2024-2025.

!!! note "Microsoft AI Tour 2024 Registration Is Live"

    The workshop is offered as an **instructor-led** session (WRK550) on the **Prototype to Production** track:

    > Use Azure AI Studio to build, evaluate, and deploy a customer support chat app. This custom copilot uses a RAG architecture built with Azure AI Search, Azure CosmosDB and Azure OpenAI to return responses grounded in the product and customer data.

    - [**Register to attend**](https://aitour.microsoft.com/) at a tour stop near you.
    - [**View Lab resources**](https://aka.ms/aitour/wrk550) to continue your journey.

If you're not a workshop participant at AI Tour, visit [github.com/Azure-Samples/contoso-chat](https://github.com/Azure-Samples/contoso-chat/blob/main/README.md) for a version of this workshop you can run using your own Azure subscription. TODO: UPDATE FOR SELF-GUIDED WORKSHOP LINK.

## Pre-Requisites

To participate in this workshop, you will need:

1. Your own laptop.
   * It need only be capable of running a browser and GitHub Codespaces, so almost any laptop will do.
   * A recent version of Edge, Chrome or Safari is recommended.
1. A GitHub Account.
   * If you don't have one, you can [signup for a free account](https://github.com/signup) now.
   * After this workshop is complete, you will have a fork of the "contoso-chat" repository in your GitHub account, which includes all the materials you will need to reproduce this workshop at home.
1. Familiarity with Visual Studio Code. 
   * We will run all code in GitHub Codespaces, a virtualized Linux machine, instead of your local laptop. We won't be running anything on your laptop directly.
   * VS Code Online will be our development environment in GitHub Codespaces.
   * If you are familiar with running Codespaces within VS Code Desktop on your laptop, feel free to do so. 
1. (preferred) Familiarity with the `bash` shell. 
    * We'll be using `bash` to run commands in the VS Code terminal.

## Get Started

We won't be using the virtual machine you see to the left to these instructions. **There is no need to log in.**

TIP: Open the "hamburger" menu in the top-right of this window, and choose "Split Windows". You can then minimize (but **do not close**) the virtual machine window.

1. Open a new browser window on your laptop. 

1. Click the link in green to copy it to your clipboard: ++https://github.com/Azure-Samples/contoso-chat++

1. Paste the link in your browser to open the GitHub repository.

1. **Sign in** to GitHub if you aren't logged in already, using your own GitHub account credentials.

1. Click **Fork** in the top-right corner of the page

1. In the **Create a new fork** page, scroll down and **uncheck** the option "Copy the `main` branch only", and then click **Create Fork**.

   * **Important**: If you forgot to uncheck that option, you will need to delete your fork and try again. Ask a proctor for assistance.

   * You should now be at the page `https://github.com/YOURUSERNAME/contoso-chat` within your own GitHub account.
   
   * You now have a copy (known as a fork) of this workshop repository in your own GitHub account! Feel free to play with it, you won't break anything.

1. Use the branch selection drop-down on the left side that now reads **main** and select the branch **aitour-fy25**.

1. Click the green **<> Code** button in the top-right part of the page, click the **Codespaces** tab, and then click **Create codespace on aitour-fy25**.

1. This step takes a few minutes. The instructor will give you an overview of the session, and then you can begin work on your own in the Codespaces environment in your browser when it's ready.

## Azure Credentials

We have created a temporary Azure subscription for you to use during this workshop. 

Login to your VM with the following credentials...

**Username: +++@lab.VirtualMachine(Win11-Pro-Base-VM).Username+++**

**Password: +++@lab.VirtualMachine(Win11-Pro-Base-VM).Password+++** 

Cloud log in

++portal.azure.com++

++azd auth login --use-device-code++

++azd up --no-prompt --e AITOUR++

++@lab.CloudPortalCredential(User1).Username++

++@lab.CloudPortalCredential(User1).Password++

## Continue the workshop

In your Codespace, use the VS Code Online File Explorer on the left to open the file `docs\index.md`.


Follow the instructions in that file to continue. 

