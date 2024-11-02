# 2. The RAG Pattern

Foundation large language models are trained on massive quantities of public data, giving them the ability to answer general questions effectively. However, our retail copilot needs responses grounded in _private data_ that exists in the retailer's data stores. _Retrieval Augmented Generation_ (RAG) is a design pattern that provides a popular solution to this challenge with this workflow:

1. The user query arrives at our copilot implementation via the endpoint (API).
1. The copilot sends the text query to a **retrieval** service which vectorizes it for efficiency.
1. It uses this vector to query a search index for matching results (e.g., based on similarity)
1. The retrieval service returns results to the copilot, potentially with semantic ranking applied.
1. The copilot **augments** the user prompt with this knowledge, and invokes the chat model.
1. The chat model now **generates** responses _grounded_ in the provided knowledge.

![RAG](./../img/rag-design-pattern.png)
 