# 6️⃣ | Deploy with ACA

??? success "Step 1: Explore the Codebase"

    - The Contoso Chat app is deployed as an Azure Container App (shown prior)
    - It is implemented as a FASTAPI endpoint with two routes ("/" and "/api/create_response")
    - View the `src/api/main.py` to learn about the parameters expected by the latter
    - View the `src/api/product/product.py` to see information retrieval for RAG pattern usage
    - View the `src/api/contoso_chat/chat_request.py` to see main chat AI workflow orchestration

??? success "Step 2: Test Endpoint Locally"

    1. Let's run the server locally, for testing:
        - change directories to the root of your repo
        - run this command: `fastapi dev src/api/main.py`
        - you should see a popup dialog - click "Open in Browser"
        - you should see: the default "Hello World" page (route=`/`)
    1. Add a `/docs` suffix to page URL - you should see: **FastAPI** page
    1. Expand the `POST` section by clicking the arrow
        - click `Try it out` to make inputs editable
        - enter `Tell me about your tents` for **question**
        - enter `2` for **customer_id**
        - enter []` for **chat_history**
        - enter **Execute** to run the query
    1. You should get a valid response with `answer` and `context`.
    1. ✅ | You just tested your Contoso Chat app with valid inputs!

??? success "Step 3: Make changes & test (awareness only)"
    
    1. Make changes to `main.py` - e.g., change "Hello World" to "Hello AI Tour!"
    1. Run `fastapi dev src/api/main.py` again to see changes
        - default route at "/" now shows updated message
    1. The repository uses `azd` for deployment - learn more in the docs.
    
---
