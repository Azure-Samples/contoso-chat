# Welcome, Learners!

This website contains the step-by-step instructions for a workshop that teaches you how to build, evaluate, and deploy, a RAG-based retail copilot - code-first, on Azure AI.

---

## Application Scenario

Contoso Outdoors is an enterprise retailer that sells a wide variety of hiking and camping equipment to outdoor adventurers. Their website has an extensive catalog of items, and sees a lot of traffic from customers looking for information and recommendations to make purchases.

![Contoso Chat UI](./img/chat-ui.png)

Contoso Chat is the implementation of a customer support chatbot that serves this purpose. Customers can ask the chatbot questions about product items _in natural language_, and get back responses that are grounded in the retailer's product catalog and their own purchase history.

![Contoso Chat AI](./img/chat-ai.png)

---
 
## Application Architecture

The figure shows the application architecture for the Contoso Chat Retail Copilot. User requests come into the chat AI (backend) through the Azure Container Apps endpoint from authenticated clients (chat UI). The request is converted to a vectorized query (using Embeddings models) and used to **retrieve** relevant product data (with similarity search) and customer data (from a noSQL database) - which are then used to **augment** the initial request. This enhanced prompt is now sent to chat model, to generate the final response sent back to the user.

![ACA Architecture](./img/aca-architecture.png)

The solution should support multi-turn conversational exchanges (with context) and support responsible AI practices, to deliver responses that meet desired quality and safety standards.

---

## Workshop Delivery 

The workshop is currently designed for delivery in two different contexts:

1. [Self-Guided Workshop](./self-paced.md) - work through the instructions on your own
    - You will need to have your own subscription
    - You will provision Azure infrastructure and deploy the application yourself. 
    - You can work at your own pace and explore the codebase at will.
2. [Tour-Based Workshop](tour-based.md) - offered as instructor-led sessions on the [Microsoft AI Tour](https://aka.ms/aitour). 
    - You will be provided with an Azure subscription (just bring your laptop)
    - The infrastructure will be pre-provisioned for you to save you time
    - You will have a fixed time (75 minutes) to complete the workshop.