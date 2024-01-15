# 1 | Debug Issues

!!!warning "Don't see your issue listed?"

    [Submit an issue](https://github.com/Azure-Samples/contoso-chat/issues/new/choose) to the repository with the following information, to help us debug and update the list

     - Which workshop section were you on? (e.g., Setup Promptflow)
     - What step of that section were you on? 
     - What was the error message or behavior you saw?
     - What was the behavior you expected?
     - Screenshot of the issue (if relevant).
    
    When submitting any issue please make sure you mask any secrets or personal information (e.g., your Azure subscription id) to avoid exposing that information publicly.

This page lists any frequently-encountered issues for this workshop, with some suggestions on how to debug these on your own. Note that Azure AI Studio (Preview) and Promptflow are both evolving rapidly - some known issues may be resolved in future updates to those tools.

---

## 1. Model Deployments

!!!bug "1.1 | Requested Model Not Found"

- **What Happened:**
    - Required model does not show in options for Create
- **Possible Causes:**
    - Model not available in region where the Azure AI resource is provisioned
    - Model available but no quota left in subscription
- **Debug Suggestions:**
    - Open "Manage" page under Azure AI Studio
    - Pick "Quota" tab, select your subscription
    - Check quota for region Azure AI resource is in
    - If none left, look for region that still has quota
    - Switch to that region and try to create deployment.

