FROM  python:3.11-slim

WORKDIR /app

COPY requirements.txt .

COPY azure_core-1.31.0-py3-none-any.whl .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --force-reinstall azure_core-1.31.0-py3-none-any.whl

#copy product folder
COPY ./contoso_chat/product /app/product
COPY . .

EXPOSE 80

CMD ["fastapi", "run", "main.py", "--port", "80"]
