# Contoso-Chat Workshop 
This folder contains the content for the Contoso-Chat workshop. It is written in Markdown using the [mkdocs Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/?h=ad) extensions. 

You can read this content with any Markdown viewer (for example, Visual Studio Code or GitHub). Start here: [Build a Retail Copilot Code-First on Azure AI](docs/index.md).

For the best experience build the documentation and view it in a browser window using the instructions below.

## How to Buid the Workshop Content from CodeSpaces

Using CodeSpaces on this repository, you can do this as follows:

```
cd docs/workshop
mkdocs serve -a localhost:5000
```

VS Code will prompt to open the content in a browser window for you.


## How to Buid the Workshop Content in your own Environment

You will need to install `mkdocs-material` first:

```
pip install mkdocs-material
```

Then, follow the Codespaces instructions above to launch the server. Open a browser on `http://localhost:5000/` to view the content.

