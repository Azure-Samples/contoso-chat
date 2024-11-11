FROM  python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY ../../packages/whl-packages/azure_ai_inference-1.0.0b6-py3-none-any.whl ./packages/whl-packages/azure_ai_inference-1.0.0b6-py3-none-any.whl
COPY ../../packages/whl-packages/azure_ai_projects-1.0.0b1-py3-none-any.whl ./packages/whl-packages/azure_ai_projects-1.0.0b1-py3-none-any.whl

RUN pip install --no-cache-dir -r requirements.txt

#copy product folder
COPY ./contoso_chat/product /app/product
COPY . .

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]
