# 08. VSCode Azure Login

> [!NOTE]
_This assumes you did the **[02. Launch GitHub Codespaces](#2-launch-github-codespaces)** step previously and left that tab open for dev container setup to complete._

* []  **01** | Switch browser tab to your Visual Code editor session
    - You should see a Visual Studio Code editor 
    - You should see a terminal open in editor

> [!hint]
> If VS Code Terminal is not open by default, click hamburger menu (top left), look for _Terminal_ option & Open New Terminal.

* []  **02** | Use Azure CLI from terminal, to login
    - Enter command: +++az login --use-device-code+++ 
    - Open +++https://microsoft.com/devicelogin+++ in new tab
    - Copy-paste code from Azure CLI into the dialog you see here
    - On success, close this tab and return to VS Code tab

---

🥳 **Congratulations!** <br/> You're logged into Azure on VS Code.