# 6️⃣ | Deploy with ACA

# Step 1: Explore the Codebase

The Contoso Chat app is deployed as an Azure Container App (now in Tab 5️⃣)

- It is implemented as a FASTAPI endpoint with two routes ("/" and "/api/create_response")
- View the `src/api/main.py` to learn about the parameters expected by the latter
- View the `src/api/product/product.py` to see information retrieval for RAG pattern usage
- View the `src/api/contoso_chat/chat_request.py` to see main chat AI workflow orchestration

# Step 2: Test Endpoint Locally

1. Let's run the server locally, for testing:
    - change directories to the root of your repository
    - run this command:
    ```
    fastapi dev src/api/main.py
    ```
    - you should see a popup dialog - click "Open in Browser"
    - you should see: the default "Hello World" page (route=`/`)

    !!! success "You just launched the endpoint within Codespaces for testing!"

1. Add a `/docs` suffix to page URL - you should see: **FastAPI** page
1. Expand the `POST` section by clicking the arrow
    - click `Try it out` to make inputs editable
    - enter `Tell me about your tents` for **question**
    - enter `2` for **customer_id**
    - enter `[]` for **chat_history**
    - enter **Execute** to run the query
1. You should get a valid response with `answer` and `context`.

!!! success "You just tested your Contoso Chat app with valid inputs!"

Step 3: Make changes & test effects locally
    
1. Make changes to `main.py` - e.g., change "Hello World" to "Hello AI Tour!"
1. Run `fastapi dev src/api/main.py` again to see changes
    - default route at "/" now shows updated message
1. The repository uses `azd` for deployment - learn more in the docs.
    
---

_You made it!. That was a lot to cover - but don't worry! Now that you have a fork of the repo, you can check out the [Self-Guided Workshop](./../02-Self-Guide-Setup/01-setup.md) option to revisit ideas at your own pace! Before you go, some important cleanup tasks you need to do!!_


!!! example "Next → [Summary & Teardown](./../04-Workshop-Wrapup/07-cleanup.md) - and thank you all for your attention!"