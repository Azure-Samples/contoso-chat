# Part 0: Preprovision Resources (Deconstructing Contoso Chat - An Interactive Workshop)

This document describes the steps needed for lab-organizers or self-guided participants to pre-provision resources. 

For workshops with multiple users, each participant will need an Azure account, and you will need to follow these instructions for each participant.

## Required Resources

TODO: Provide a list of resources that will be deployed here, and give an indication of cost for those resources.

## Deploy Azure Resources

**Clone** the contents of this repository to the terminal. 
   * Skip this step if using CodeSpaces (this has already been done for you)

```
git clone https://github.com/revodavid/contoso-chat/tree/aitour-fy25
```

**Log in** to the Azure Subscription the participant will use for the workshop. You can use any of:

   * [Azure Cloud Shell](https://learn.microsoft.com/azure/cloud-shell/overview)
   * Any terminal with [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/) installed
   * [GitHub Codespaces](https://docs.github.com/codespaces/overview) launched on the **aitour-fy25** branch of `https://github.com/revodavid/contoso-chat`

If not using Azure Cloud Shell, you can use the commands below (both are required)

```
azd auth login --use-device-code
```
```
az login --use-device-code
```

**Configure deployment**

In this step we will create an [AZD environment](https://learn.microsoft.com/azure/developer/azure-developer-cli/manage-environment-variables#environment-specific-env-file) called AITOUR to store configurations. This will also capture needed resource information after deployment in the file `.azure\AITOUR\.env`.

Choose a **region** that provides the required resources and in which the subscriptions have sufficient quote available. In the example below, we use the `--location` parameter to select the region **francecentral**.

```
azd env new AITOUR --location francecentral --subscription $(az account show --query id --output tsv)
```

TODO: Does this work? If so we won't need the `az login` step.
```
azd env new AITOUR --location francecentral --subscription $(azd env get-value AZURE_SUBSCRIPTION_ID)
```

**Deploy resources**

Now that yo have selected a region, begin the deployment with the command below. 

```
azd up -e AITOUR --no-prompt
```

Wait until provisioning completes. This can take 30-40 minutes depending on region.

### Troubleshooting

#### Failed: Key Vault

If you get an error like this:

```
  (x) Failed: Key Vault: kv-ga6xwbwbqulka
```

during `azd up`, it may be because a prior deployment in the same region used the same name, and the key-vault has been soft-deleted but not purged. You will need to purge the keyvault:

```
az keyvault purge -n kv-ga6xwbwbqulka
```

Once the purge completes, run the `azd up` command again.

#### InvalidTemplateDeployment: The template deployment 'cognitiveServices' is not valid according to the validation procedure.

If you get an error like:
```
FlagMustBeSetForRestore: An existing resource with ID '/subscriptions/265d8bce-3441-475d-8ee1-a1037b8c3eae/resourceGroups/rg-AITOUR/providers/Microsoft.CognitiveServices/accounts/aoai-ga6xwbwbqulka' has been soft-deleted. To resto1re the resource, you must specify 'restore' to be 'true' in the property. If you don't want to restore existing resource, please purge it first.
```

Purge the resource as follows:
* Go to the portal
* search for "Azure AI Service" and select the one with the logo (not the one with the cloud)
* click Manage Deleted Resources
* select the named resource
* click purge.

You should be able to purge with this command, but it doesn't seem to work.
```
az resource delete --ids /subscriptions/265d8bce-3441-475d-8ee1-a1037b8c3eae/resourceGroups/rg-AITOUR/providers/Microsoft.CognitiveServices/accounts/aoai-ga6xwbwbqulka
```

You can also search for 



## Capture environment

If the participant is not going to use the same filesystem just used to deploy (for example, they will log into a different machine, or launch a new instance of CodeSpaces), you will need to capture the environment file and provide it to their workspace.

1. Capture the file `.azure/AITOUR/.env` after deployment is complete
2. Install the file to `.azure/AITOUR/.env` in the student's filesystem

How you do this depends on lab format. Options include:

* Take no action, and continue the workshop in the same filesystem used to deploy resources (ideal for self-guided participants)
* Upload the file to Azure storage, and provide instructions for participants to download and install it on their system
* Embed the contents of the `.env` file in the lab instructions, and ask participants to paste in the contents to the file `.azure/AITOUR/.env`

## Next step

If you are a self-guided student, congratulations! You have completed the provisioning step.

Continue to [1-GetStarted.md](1-GetStarted.md) to start the workshop experience.

Once you've finished with the workshop, visit [3-CleanUp.md](3-CleanUp.md) for information on how to delete the Azure resources.