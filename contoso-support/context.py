from promptflow import tool

@tool
def context(citations: object, customer_data: object) -> str:
  return {"citations": citations, "customer_data": customer_data}
