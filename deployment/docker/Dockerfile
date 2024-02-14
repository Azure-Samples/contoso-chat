FROM mcr.microsoft.com/azureml/promptflow/promptflow-runtime-stable:latest
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt