# 5. The Dev Workflow

In this workshop, we'll follow a simplified version of the development lifecycle as shown in the figure below. For each stage of our development, we'll talk about the **task** we need to perform, and the **tool** that helps us do this.

![Dev Workflow](./../img/dev-workflow.png)

Let's briefly review these stages:

1. **Provision** - sets up our Azure infrastructure and deploys the initial application. The Azure Developer CLI _infrastructure-as-code_ approach makes this consistently reproducible.
1. **Setup** - sets up our development environment and configures it to work with the provisioned infrastructure. The **Dev Container** _configuration-as-code_ approach makes this effortless.
1. **Ideate** - takes us from first prompt to functional prototype, validating our model choice for the app scenario. The **Prompty** asset & tooling makes it easy to iterate & refine our prompts.
1. **Evaluate** - lets us assess the quality of our prototype using larger test datasets with AI-assisted evaluation flows. The **Prompty** asset helps makes custom evaluator creation easy.
1. **Deploy** - lets us move the prototype to production with a hosted API endpoint accessible to real-world clients. Using **Azure Container App** with `azd` makes this process seamless.

We should also keep _Trustworthy AI_ considerations in mind throughout the end-to-end development workflow - from selecting models from trusted partners, to using managed identity (keyless authentication), building custom evaluators (for assessments) and leveraging safety systems (for content filtering). Check out the [Learning Resources](./../index.md#learning-resources) for more information.