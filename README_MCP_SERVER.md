# Awesome GitHub Copilot MCP Server

A Model Context Protocol (MCP) server that provides access to the extensive collection of GitHub Copilot prompts from the [awesome-copilot repository](https://github.com/github/awesome-copilot). This server exposes over 35 carefully curated prompts as tools and resources, making them easily discoverable and usable in any MCP-compatible environment.

## Features

### 🎯 **35+ Professional Prompts**
Access a comprehensive collection of prompts covering:
- **Development**: Spring Boot projects, ASP.NET APIs, multi-stage Dockerfiles
- **Testing**: Jest, NUnit, XUnit, MSTest best practices
- **Documentation**: Component docs, specifications, ADRs, llms.txt files
- **Best Practices**: .NET/C#, async programming, Entity Framework Core
- **Project Management**: Implementation plans, GitHub issues, specifications
- **Cloud & DevOps**: Azure optimization, Bicep modules, Docker containers
- **GitHub Workflows**: Pull requests, issues, repository management

### 🔍 **Smart Discovery**
- **Search by keywords**: Find prompts by title, description, or category
- **Filter by category**: Browse prompts by type (development, testing, documentation, etc.)
- **Tool-based filtering**: Find prompts that use specific VS Code tools
- **Metadata access**: Get detailed information about each prompt

### 📚 **Rich Resources**
- Complete prompt registry with metadata
- Category-based organization
- Installation instructions for VS Code
- Usage guidelines and examples

### 🛠️ **Practical Tools**
- Search and discovery functions
- Installation URL generation
- Usage guide generation
- Tool compatibility checking

## Installation

### Prerequisites
- Python 3.8+
- MCP-compatible client

### Setup

1. **Install dependencies:**
```bash
pip install -r requirements_mcp.txt
```

2. **Run the server:**
```bash
python awesome_copilot_mcp_server.py
```

3. **Test with MCP Inspector:**
```bash
npx @modelcontextprotocol/inspector python awesome_copilot_mcp_server.py
```

## Usage

### Resources

#### List All Prompts
```
copilot-prompts://list
```
Returns a JSON list of all available prompts with basic metadata.

#### Get Prompts by Category
```
copilot-prompts://development
copilot-prompts://testing
copilot-prompts://documentation
copilot-prompts://best-practices
copilot-prompts://project-management
copilot-prompts://github
copilot-prompts://cloud
copilot-prompts://devops
```

#### Get Prompt Details
```
copilot-prompts://prompt/{prompt_id}
```
Returns detailed information about a specific prompt including installation URLs.

#### List Categories
```
copilot-prompts://categories
```
Returns all available categories with prompt counts.

### Tools

#### Search Prompts
```python
search_prompts(query="spring boot", category="development")
```
Search for prompts by keywords with optional category filtering.

#### Get Installation Instructions
```python
get_prompt_installation_instructions("create-spring-boot-java-project")
```
Get VS Code installation URLs and usage instructions for any prompt.

#### Find Prompts by Tools
```python
get_prompts_by_tools(["codebase", "editFiles", "problems"])
```
Find prompts that support specific VS Code tools.

#### Generate Usage Guide
```python
generate_prompt_usage_guide(category="testing")
```
Generate a comprehensive markdown guide for prompts in a category.

### Prompts

#### Find Development Prompts
Find development-related prompts for specific languages or frameworks.

#### Setup GitHub Workflow Prompts  
Find prompts for GitHub workflow automation and project management.

#### Documentation Prompts Setup
Find and recommend documentation-related prompts.

## Available Prompt Categories

### 🔧 Development (5 prompts)
- **ASP.NET Minimal API with OpenAPI**: Create API endpoints with documentation
- **Create Spring Boot Java/Kotlin Projects**: Project scaffolding and setup
- **Next.js Internationalization**: Add language support to Next.js apps
- **Multi-stage Dockerfiles**: Optimized container builds

### 🧪 Testing (4 prompts)
- **Jest Best Practices**: JavaScript/TypeScript testing
- **NUnit/XUnit/MSTest**: C#/.NET testing frameworks
- **Test Structure and Patterns**: Comprehensive testing guidance

### 📖 Documentation (8 prompts)
- **Component Documentation**: Standardized OO component docs
- **LLMs.txt Generation**: Repository navigation for AI
- **Specification Creation**: AI-optimized specifications
- **Tutorial Generation**: Code-to-tutorial transformation
- **Architectural Decision Records**: Decision documentation

### ✨ Best Practices (5 prompts)
- **.NET/C# Guidelines**: Code quality and patterns
- **Async Programming**: C# async/await best practices
- **Entity Framework Core**: ORM optimization
- **Design Pattern Review**: Architecture analysis

### 📋 Project Management (4 prompts)
- **Implementation Planning**: Feature and refactoring plans
- **GitHub Issue Creation**: Automated issue generation
- **Specification Requirements**: Requirement tracking

### 🐙 GitHub Integration (2 prompts)
- **My Issues/Pull Requests**: Personal GitHub workflow
- **Repository Management**: GitHub workflow automation

### ☁️ Cloud & DevOps (3 prompts)
- **Azure Cost Optimization**: Resource cost analysis
- **Azure Bicep Modules**: Infrastructure updates
- **Container Optimization**: Docker best practices

## Examples

### Find Testing Prompts
```python
# Search for testing-related prompts
results = search_prompts("testing", category="testing")

# Get installation instructions for NUnit prompt
install_info = get_prompt_installation_instructions("csharp-nunit")

# Generate testing guide
guide = generate_prompt_usage_guide(category="testing")
```

### Discover Documentation Tools
```python
# Find prompts that work with codebase editing
doc_prompts = get_prompts_by_tools(["codebase", "editFiles"])

# Get details about LLMs.txt prompt
llms_prompt = get_prompt_details("create-llms")
```

### GitHub Workflow Setup
```python
# Find all GitHub-related prompts
github_prompts = search_prompts("github", category="github")

# Get project management prompts
pm_prompts = search_prompts("", category="project-management")
```

## Integration Examples

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "awesome-copilot": {
      "command": "python",
      "args": ["/path/to/awesome_copilot_mcp_server.py"],
      "env": {}
    }
  }
}
```

### Continue.dev Integration
Add to your Continue configuration to access prompts in your IDE.

### Custom MCP Client
```python
import asyncio
from mcp.client.session import ClientSession

async def use_awesome_copilot():
    async with ClientSession() as session:
        # List all prompts
        prompts = await session.read_resource("copilot-prompts://list")
        
        # Search for specific prompts
        results = await session.call_tool("search_prompts", {
            "query": "spring boot",
            "category": "development"
        })
        
        # Get installation instructions
        install = await session.call_tool("get_prompt_installation_instructions", {
            "prompt_id": "create-spring-boot-java-project"
        })
```

## Contributing

This MCP server is based on the [awesome-copilot repository](https://github.com/github/awesome-copilot). To contribute:

1. **Add new prompts**: Contribute to the upstream awesome-copilot repository
2. **Update server**: Submit PRs to update the prompt registry in this server
3. **Report issues**: File issues for missing prompts or incorrect metadata

## License

This project follows the same license as the awesome-copilot repository. The prompts and content are from the GitHub awesome-copilot project.

## Related Projects

- [awesome-copilot](https://github.com/github/awesome-copilot) - The source repository for all prompts
- [Model Context Protocol](https://modelcontextprotocol.io/) - The protocol specification
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - The SDK used to build this server

---

**Note**: This is an unofficial MCP server that provides access to the awesome-copilot prompts. For the latest prompts and official content, visit the [awesome-copilot repository](https://github.com/github/awesome-copilot).
