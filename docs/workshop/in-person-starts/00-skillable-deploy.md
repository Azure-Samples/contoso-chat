<!-- This was the docs/skillable-getstarted-deploy.md file from aitour-fy25 -->

# Build a Retail Copilot Code-First on Azure AI

These instructions are forcontent owners of the Workshop "Build a Retail Copilot Code-First on Azure AI" at Microsoft AI Tour 2024-2025.

TODO: UPDATE SKILLABLE LAB TO POINT TO github.com/Azure-Samples/contoso-chat/docs/skillable-getstarted-deploy.md

## Pre-Requisites

To participate in this workshop, you will need:

1. Your own laptop.
   * It need only be capable of running a browser and GitHub Codespaces, so almost any laptop will do.
   * A recent version of Edge, Chrome or Safari is recommended.
1. A GitHub Account.
   * If you don't have one, you can [sign up for a free account](https://github.com/signup) now.
   * After this workshop is complete, you will have a fork of the "contoso-chat" repository in your GitHub account, which includes all the materials you will need to reproduce this workshop at home.
1. (recommended) Familiarity with Visual Studio Code. 
   * We will run all code in GitHub Codespaces, a virtualized Linux machine, instead of your local laptop. We won't be running anything on your laptop directly.
   * VS Code Online will be our development environment in GitHub Codespaces.
   * If you are familiar with running Codespaces within VS Code Desktop on your laptop, feel free to do so. 
1. (preferred) Familiarity with the `bash` shell. 
    * We'll be using `bash` to run commands in the VS Code terminal.
1. (preferred) Familiarity with Python and Jupyter Notebooks
    * We'll be creating Python scripts and running them from the command line and from Notebooks.

## Get Started

We won't be using the Azure Portal window to the left of these instructions. **You can close that window now.**

## Log into GitHub Codespaces

GitHub Codespaces will be our development environment for this workshop. You will need to log into your own GitHub account and copy (fork) the workshop materials to your account. Let's do that now.

1. **Open a new browser window** on your laptop. 

1. **Click the link** below to copy it to your clipboard: 
    * ++https://github.com/Azure-Samples/contoso-chat++
    * TODO FIX: for the WIP version, fork ++https://github.com/Azure-Samples/contoso-chat++ instead.

1. **Paste the link in your browser** to open the GitHub repository.

1. **Sign in to GitHub** if you aren't logged in already, using your own GitHub account credentials.

1. Click **Fork** in the top-right corner of the page

1. In the "Create a new fork" page, scroll down and **uncheck** the option "Copy the main branch only".

   * **Important**: If you forget to uncheck that option, you will need to delete your fork and try again. Ask a proctor for assistance.

1. Click the **Create Fork** button.

   * You should now be at the page `https://github.com/YOURUSERNAME/contoso-chat` within your own GitHub account.
   
   * You now have a copy (known as a fork) of this workshop repository in your own GitHub account! Feel free to play with it, you won't break anything.

1. Use the branch selection drop-down on the left side that now reads **main** and select the branch **aitour-fy25**.

1. Click the green **<> Code** button in the top-right part of the page, click the **Codespaces** tab, and then click **Create codespace on aitour-fy25**.

1. This step takes a few minutes. The instructor will give you an overview of the session, and then you can begin work on your own in the Codespaces environment in your browser when it's ready.

## Blank deployment (TODO delete)

From Powershell:

Log into VM:

+++@lab.VirtualMachine(WRK550-Win11(NEW)).Password+++

Launch `cmd` in VM.

Delete an existing contoso-chat folder if it exists.

+++git clone -b aitour-fy25 --single-branch https://github.com/revodavid/contoso-chat+++

+++cd contoso-chat+++

+++azd env new AITOUR --location francecentral+++

Log in with Azure Credentials below:

+++azd auth login+++

+++azd up -e AITOUR+++

Select default subscription, press ENTER.

## Full Virtual Machine (not needed TODO delete)

+++@lab.VirtualMachine(WRK550-Win11(NEW)).Username+++

+++@lab.VirtualMachine(WRK550-Win11(NEW)).Password+++

## Azure Credentials

We have created a temporary Azure subscription for you to use during this workshop. You will need these credentials shortly to log into Azure.

Username: ++@lab.CloudPortalCredential(User1).Username++

Password: ++@lab.CloudPortalCredential(User1).Password++

## Continue the workshop

In your Codespace, use the VS Code Online File Explorer on the left to open the file `docs\2-Instructions.md`.

Follow the instructions in that file to continue. 