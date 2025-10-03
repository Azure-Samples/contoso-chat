# AGENTS.md

## Project Overview

Contoso Chat is a retail RAG (Retrieval Augmented Generation) copilot application built with Azure AI Foundry and Prompty. The application serves as a customer service chatbot for Contoso Outdoor, an online retailer specializing in hiking and camping equipment. It uses a retrieval augmented generation pattern to ground chatbot responses in the retailer's product catalog and customer purchase history.

**Key Technologies:**
- **Language**: Python 3.10+
- **API Framework**: FastAPI
- **AI/ML**: Azure OpenAI (gpt-4, gpt-4o-mini, text-embedding-ada-002), Prompty
- **Data Storage**: Azure Cosmos DB (NoSQL), Azure AI Search (semantic search with indexes)
- **Infrastructure**: Azure Container Apps, Azure Monitor, Azure AI Foundry
- **Deployment**: Azure Developer CLI (azd), Docker
- **Development**: GitHub Codespaces, VS Code Dev Containers

**Architecture**: RAG-based copilot with semantic search over product catalogs and customer data, deployed as a FastAPI endpoint on Azure Container Apps.

## Setup Commands

### Prerequisites Installation
```bash
# Install Azure Developer CLI
# Visit: https://aka.ms/install-azd

# Install Python 3.10 or higher
# Visit: https://www.python.org/downloads/

# Install Docker Desktop
# Visit: https://www.docker.com/products/docker-desktop/

# Install Git
# Visit: https://git-scm.com/downloads/
```

### Project Initialization

**Option 1: Using GitHub Codespaces (Recommended)**
- Click the "Open in GitHub Codespaces" button in the README
- Wait for the environment to be ready (several minutes)
- All dependencies are pre-installed

**Option 2: Using VS Code Dev Containers**
- Install Docker Desktop and start it
- Click the "Open in Dev Containers" button in the README
- Wait for the container to build and start
- All dependencies are pre-installed

**Option 3: Local Environment Setup**
```bash
# Clone or initialize the project
azd init -t contoso-chat

# Install Python dependencies
cd src/api
pip install -r requirements.txt
```

### Azure Authentication
```bash
# Authenticate with Azure CLI (use --use-device-code for Codespaces)
az login --use-device-code

# Authenticate with Azure Developer CLI
azd auth login --use-device-code
```

## Development Workflow

### Azure Infrastructure Provisioning and Deployment

```bash
# Provision Azure infrastructure AND deploy the application (all-in-one)
azd up

# OR provision and deploy separately:
azd provision  # Provision Azure infrastructure only
azd deploy     # Deploy the application only

# Get environment variables (creates .env file)
azd env get-values > .env
```

**Note**: `azd up` takes 15-20 minutes on first run. You will be prompted for:
- Azure subscription
- Environment name (maps to resource group name)
- Location (recommended: `eastus2` or `francecentral`)

**Expected Infrastructure** (after successful provisioning):
- 35 deployments
- 15 resources including:
  - Azure AI Foundry Hub and Project
  - Azure OpenAI (with model deployments)
  - Azure AI Search (with `contoso-products` index)
  - Azure Cosmos DB (with `customers` database)
  - Azure Container Apps (hosting the API)
  - Azure Monitor (Application Insights)
  - Azure Container Registry
  - Azure Key Vault

### Local Development Server

```bash
# Start the FastAPI development server from repository root
fastapi dev ./src/api/main.py

# The server will start on http://localhost:8000
# Access the interactive API docs at http://localhost:8000/docs
```

### Using Docker Compose

```bash
# Build and run the API container
docker-compose up

# The API will be available at http://localhost:80
```

### Environment Variables

The project uses environment variables for Azure resource configuration. These are automatically populated by `azd env get-values` after provisioning. Key variables include:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_SEARCH_ENDPOINT`
- `COSMOS_ENDPOINT`
- `APPINSIGHTS_CONNECTIONSTRING`
- And many others (see `azure.yaml` pipeline section for full list)

## Testing Instructions

### Manual Testing (Interactive)

**Testing the Deployed Endpoint:**
1. Navigate to Azure Portal → Resource Group → Azure Container Apps resource
2. Click the "Application Url"
3. Add `/docs` to the URL path
4. Use the Swagger UI to test the `/api/create_response` endpoint
5. Example test input:
   - `question`: "Tell me about the waterproof tents"
   - `customer_id`: "2"
   - `chat_history`: `[]`
6. Click "Execute" to see the chatbot response

**Testing Locally:**
1. Start the dev server: `fastapi dev ./src/api/main.py`
2. Open browser to the provided URL (usually http://localhost:8000)
3. Navigate to `/docs` for the Swagger UI
4. Test the `/api/create_response` POST endpoint as described above

### AI-Assisted Evaluation (Automated)

The project includes comprehensive AI-assisted evaluation using custom evaluators built with Prompty.

```bash
# Run evaluations from the API directory
cd src/api
python -m evaluate
```

**What this does:**
- Loads test dataset from `evaluators/data.jsonl`
- Generates chatbot responses for each test question
- Evaluates responses using custom evaluators for:
  - **Coherence**: Logical flow and consistency
  - **Fluency**: Language quality and readability
  - **Relevance**: Alignment with the question
  - **Groundedness**: Factual accuracy based on context
- Outputs results to:
  - `result.jsonl`: Raw chatbot responses
  - `result_evaluated.jsonl`: Responses with evaluation scores
  - `eval_results.jsonl`: Final evaluation results
  - `eval_results.md`: Human-readable summary with average scores

**Using the Evaluation Notebook:**
```bash
# Open and run the evaluation notebook
# Location: src/api/evaluators/evaluate-chat-flow.ipynb
# Select kernel, clear inputs, then "Run All"
# Evaluation takes 10+ minutes to complete
```

**Tracing and Observability:**
- Prompty provides built-in tracing
- Trace files are saved in `.runs/` subfolder as `.tracy` files
- Click a trace file in VS Code to view detailed execution flow

### CI/CD Testing

The repository includes GitHub Actions workflows for automated evaluation:
- Location: `.github/workflows/evaluations.yaml`
- Trigger: Push to `main` branch or manual dispatch
- Runs the evaluation suite automatically
- Uploads results as build artifacts

## Code Style

### Python Conventions
- **Python Version**: 3.10+
- **Code Style**: Follow standard Python conventions (PEP 8)
- **Type Hints**: Not strictly enforced but recommended

### File Organization
```
src/api/
  ├── main.py                    # FastAPI application entry point
  ├── contoso_chat/              # Main application module
  │   ├── chat_request.py        # Chat request handler
  │   ├── chat.prompty           # Prompty template for chat
  │   └── product/               # Product search functionality
  ├── evaluators/                # Evaluation framework
  │   ├── data.jsonl             # Test dataset
  │   ├── custom_evals/          # Custom evaluator implementations
  │   └── evaluate-chat-flow.ipynb
  ├── evaluate.py                # Evaluation script
  ├── requirements.txt           # Python dependencies
  └── Dockerfile                 # Container definition
```

### Prompty Assets
- Prompty files (`.prompty`) define prompt templates
- Located alongside the code that uses them
- Include template structure, model configuration, and sample data
- Used for rapid prototyping and iteration on AI prompts

### Import Patterns
- Use absolute imports from the project root
- FastAPI decorators for route definitions
- Prompty's `@trace` decorator for observability

## Build and Deployment

### Docker Build

**Dockerfile Location**: `src/api/Dockerfile`

```dockerfile
# Build process:
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["fastapi", "run", "main.py", "--port", "80"]
```

**Build manually:**
```bash
cd src/api
docker build -t contoso-chat-api .
docker run -p 80:80 --env-file .env contoso-chat-api
```

### Azure Deployment

**Primary deployment method**: Azure Developer CLI (azd)

```bash
# Deploy to Azure Container Apps
azd deploy

# Full provision + deploy
azd up
```

**What happens during deployment:**
- Application is containerized using the Dockerfile
- Image is built remotely (remote build enabled in `azure.yaml`)
- Image is pushed to Azure Container Registry
- Container is deployed to Azure Container Apps
- Environment variables are configured from `azure.yaml` pipeline variables

**Post-provision hooks:**
- Script: `infra/hooks/postprovision.sh` (or `.ps1` for Windows)
- Generates `.env` file with Azure resource values
- Runs automatically after infrastructure provisioning

**Post-deploy hooks:**
- Script: `infra/hooks/postdeploy.sh` (or `.ps1` for Windows)
- Runs after successful deployment

### Infrastructure as Code

- **Provider**: Azure Bicep
- **Location**: `infra/` directory
- **Main template**: `infra/core/host/ai-environment.bicep`
- **Configuration**: `azure.yaml` at repository root

### Environment Configurations

The project uses a single environment managed by Azure Developer CLI:
- Environment name is specified during `azd up`
- Maps to an Azure resource group named `rg-{ENVNAME}`
- All environment variables are stored in `.azure/{ENVNAME}/.env`
- Use `azd env get-values` to export to local `.env` file

## Security Considerations

### Authentication and Identity
- **Managed Identity**: Used for authentication with Azure services
  - Azure OpenAI
  - Azure AI Search
  - Azure Cosmos DB
- No credentials stored in code or configuration
- Eliminates credential management complexity

### Secrets Management
- Secrets are stored in Azure Key Vault
- Environment variables reference Key Vault secrets
- Never commit credentials to source control

### Security Scanning
- GitHub Actions includes security scanning via `microsoft/security-devops-action`
- Scans infrastructure-as-code (Bicep files) for security issues
- Recommended: Enable GitHub secret scanning in repository settings

### Content Safety
- Azure OpenAI Content Safety integration available
- Responsible AI practices implemented
- See `RESPONSIBLE_AI.md` for guidelines (if present)

### Important Security Notice
- This is a **sample/template application**
- **Not production-ready** without additional security hardening
- Uses preview features (see Azure Preview Terms)
- Review [Azure AI security best practices](https://learn.microsoft.com/azure/developer/ai/get-started-securing-your-ai-app) before production use

## Pull Request Guidelines

### Before Submitting
1. Test locally using `fastapi dev ./src/api/main.py`
2. Verify the API works correctly via `/docs` endpoint
3. If modifying evaluation logic, run `python -m evaluate` to ensure tests pass
4. Review changes for any hardcoded credentials or secrets

### Commit Messages
- Use clear, descriptive commit messages
- Reference issue numbers when applicable

### Required Checks
- Code must not introduce security vulnerabilities
- Maintain compatibility with existing Azure infrastructure
- Follow existing code patterns and structure

## Debugging and Troubleshooting

### Common Issues

**Issue**: Azure provisioning fails due to quota or region availability
- **Solution**: Use recommended regions: `eastus2` or `francecentral`
- Check [region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) for required models

**Issue**: Local development fails to connect to Azure resources
- **Solution**: Ensure you've run `azd env get-values > .env` to populate environment variables
- Verify authentication with `az login` and `azd auth login`

**Issue**: Container build fails
- **Solution**: Ensure Docker Desktop is running
- Check that `requirements.txt` is accessible during build

### Logging and Observability

**Application Insights:**
- Configured automatically during provisioning
- Connection string available in `APPINSIGHTS_CONNECTIONSTRING` env var
- View logs and telemetry in Azure Portal

**FastAPI Logging:**
- FastAPI includes built-in logging
- View logs in terminal when running `fastapi dev`
- OpenTelemetry instrumentation enabled for distributed tracing

**Prompty Tracing:**
- Enabled by default with `@trace` decorator
- Traces saved to `.runs/` directory as `.tracy` files
- View in VS Code for debugging prompt executions

### Performance Considerations

- Azure OpenAI has rate limits based on quota
- Azure AI Search semantic ranker is a premium feature (additional cost)
- First deployment takes 15-20 minutes; subsequent deployments are faster
- Evaluation runs can take 10+ minutes depending on dataset size

## Workshop and Learning Resources

The repository includes a comprehensive workshop for learning:

**Location**: `docs/workshop/`

**Access Options:**
1. [View Online](https://aka.ms/aitour/contoso-chat/workshop)
2. View Locally:
   ```bash
   pip install mkdocs-material
   cd docs/workshop
   mkdocs serve
   # Open browser to the provided URL
   ```

**Workshop Coverage:**
- Infrastructure provisioning
- Prompt engineering and ideation
- Building and evaluating the copilot
- Deployment best practices

## Additional Notes

### Azure Services and Costs
- Most services have free tiers available
- Azure Cosmos DB: Serverless, free tier
- Azure Container Apps: Serverless, free tier
- Azure Monitor: Free tier
- Azure OpenAI: Pay-per-use (varies by region and model)
- Azure AI Search: Basic tier with Semantic Ranker (premium feature)
- Estimate costs: [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)

### Region Recommendations
- **Recommended**: `francecentral` or `eastus2`
- These regions support all required models (gpt-4, gpt-4o-mini, text-embedding-ada-002)
- Check quota availability for your subscription

### Responsible AI
- Follow Microsoft's Responsible AI guidelines
- Implement content filtering and safety measures
- Monitor for bias and fairness in responses
- Review output quality regularly

### Community and Support
- **Issues**: Submit issues via [GitHub Issues](https://github.com/Azure-Samples/contoso-chat/issues)
- **Discussions**: Use repository discussions for questions
- **Code of Conduct**: [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- **Contact**: opencode@microsoft.com for code of conduct questions

### Development Environment Tips
- **GitHub Codespaces**: Fastest setup, no local installation required
- **Dev Containers**: Good for local development with consistent environment
- **Manual Setup**: Maximum control, requires manual dependency installation
- **Git Bash**: Recommended for Windows users (for shell script compatibility)

### Quick Reference Commands

```bash
# Authentication
az login --use-device-code
azd auth login --use-device-code

# Provisioning and Deployment
azd up                           # Provision + deploy
azd provision                    # Provision only
azd deploy                       # Deploy only
azd env get-values > .env        # Export environment variables

# Local Development
fastapi dev ./src/api/main.py    # Start dev server
docker-compose up                # Run with Docker

# Testing and Evaluation
cd src/api && python -m evaluate # Run evaluations

# Verification
az version                       # Check Azure CLI
azd version                      # Check Azure Developer CLI
python --version                 # Check Python version
prompty --version                # Check Prompty version
```

### File Naming Conventions
- Python files: lowercase with underscores (`chat_request.py`)
- Prompty files: descriptive names with `.prompty` extension
- Configuration: standard names (`requirements.txt`, `Dockerfile`, `azure.yaml`)
- Data files: JSONL format for datasets (`data.jsonl`)

### Dependencies and Updates
- Dependencies defined in `src/api/requirements.txt`
- Core dependencies: fastapi, prompty, azure-* packages
- Update with caution to maintain Azure service compatibility
- Pin specific versions when stability is critical (e.g., `prompty[azure]==0.1.24`)
