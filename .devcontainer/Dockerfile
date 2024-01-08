FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install pip for Python 3.11
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install the packages
COPY requirements.txt .
RUN pip install -r requirements.txt
