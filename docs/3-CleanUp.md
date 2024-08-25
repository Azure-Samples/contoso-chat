# Part 3: Cleaning Up (Deconstructing Contoso Chat - An Interactive Workshop)

If you provisioned your own Azure resources for this workshop, you will continue to incur charges for them until you delete them. Follow these instructions to do so.

## Delete resources

**Log in** to your Azure subscription from the CLI, if not logged in already.

```
azd auth login --use-device-code
```

**Delete and purge** resources. (NOTE: If you do not purge the resources, your quote won't immediately be released.)

```
adz down --purge
```

## Delete your codespace

If you were using a Codespace to access your subscription, don't forget to delete it or you will incur consumption and storage charges on your GitHub account. This may consume your free quota, if you are using the free Codespaces benefit.

1. If you've made changes to the files in the CodeSpace and want to keep them, go to Source Control tool in the left pane to sync your changes. If you didn't fork the repository, you can choose "Fork to my account" instead.
2. Go to `https://github.com/codespaces`, find the codespace by its name at the bottom of the page, click the "..." menu, and choose **Delete**.

## You're all set

That's it! You're all cleaned up.

