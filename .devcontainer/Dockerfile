FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install pip for Python 3.11
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install the packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Necessary for promptflow keyring to work on Linux with dbus backend
RUN sudo apt-get update
RUN sudo apt-get install -y gcc cmake pkg-config libdbus-1-dev libglib2.0-dev
RUN pip install keyrings.alt dbus-python