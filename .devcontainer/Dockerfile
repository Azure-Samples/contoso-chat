# Use a specific version of Python image to ensure consistency across builds
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Combine system updates, package installations and Python upgrades into a single RUN command to reduce layers
# Also, clean up the apt cache to reduce image size
RUN sudo apt-get update && sudo apt-get install -y \
    gcc \
    cmake \
    pkg-config \
    libdbus-1-dev \
    libglib2.0-dev \
 && python -m pip install --upgrade pip \
 && sudo apt-get clean \
 && sudo rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install the Python packages
# Install keyring-related and IPython packages in the same layer to reduce the image size and build time
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && pip install keyrings.alt dbus-python ipython ipykernel

# Configure the IPython kernel
RUN ipython kernel install --name "python3" --user

# Install daily version of azd for latest changes
# See: https://github.com/Azure/azure-dev/tree/main/cli/installer#download-from-daily-builds
RUN curl -fsSL https://aka.ms/install-azd.sh | bash -s -- --version daily
