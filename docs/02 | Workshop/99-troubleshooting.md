# Troubleshooting

> [!NOTE]
_We'll use this section to list tips for troubleshooting. However, we encourage you to reach out to proctors for help. Just let them know the section and step you are stuck on._

1. **[05. Create Model Deployments](#5-create-model-deployments):** Requested Model Not Found.
    - _Possible Cause_: The model may not be available in the region you are currently using for your Azure AI Resource.
    - _To Debug This_: 
        - Open the "Manage" page on +++ai.azure.com+++ - 
        - Pick the "Quota tab", select your subscription
        - See if your target model has quota for that "Region"
        - Switch to a different "Region" - check again.
        - Do this for **all** models - pick Region that has all.
        - You may need to re-start lab with relevant Region.

