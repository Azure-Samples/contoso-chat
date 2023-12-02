from promptflow import tool

import subprocess
import sys

# Run the pip install command
def add_custom_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

import os
# List the packages installed within the current environment
packages = subprocess.check_output([sys.executable, "-m", "pip", "list"])
packages = packages.decode("utf-8")
packages = packages.split("\n")
packages = [p.split(" ")[0] for p in packages]
#packages = "\n".join(packages)


@tool
def add_packages() -> list[str]:
    add_custom_packages()
    return packages