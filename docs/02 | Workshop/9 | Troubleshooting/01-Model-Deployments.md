# 1 | Model Deployments

!!!bug "1. Requested Model Not Found"

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

