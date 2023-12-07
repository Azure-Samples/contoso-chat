FROM python:3.11-slim

# Make Python 3.11 the default
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1

# Install pip for Python 3.11
RUN python -m ensurepip
RUN python -m pip install --upgrade pip

# Copy requirements.txt and install the packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Prioritize Python 3.11.6 in the PATH
ENV PATH="/path/to/python3.11.6/bin:${PATH}"