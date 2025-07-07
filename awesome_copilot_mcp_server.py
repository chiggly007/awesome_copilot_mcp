#!/usr/bin/env python3
"""
Awesome GitHub Copilot MCP Server

This Model Context Protocol (MCP) server provides access to the prompts from the 
GitHub awesome-copilot repository as reusable tools and resources.

Based on: https://github.com/github/awesome-copilot
"""

import asyncio
import json
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP(
    "Awesome Copilot Prompts",
    dependencies=["requests", "pydantic"]
)


# Prompt registry with metadata
PROMPTS_REGISTRY = {
    "aspnet-minimal-api-openapi": {
        "title": "ASP.NET Minimal API with OpenAPI",
        "description": "Create ASP.NET Minimal API endpoints with proper OpenAPI documentation",
        "category": "development",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "az-cost-optimize": {
        "title": "Azure Cost Optimize",
        "description": "Analyze Azure resources used in the app (IaC files and/or resources in a target rg) and optimize costs - creating GitHub issues for identified optimizations",
        "category": "cloud",
        "tools": ["changes", "codebase", "editFiles", "githubRepo", "problems"]
    },
    "comment-code-generate-a-tutorial": {
        "title": "Comment Code Generate A Tutorial",
        "description": "Transform this Python script into a polished, beginner-friendly project by refactoring the code, adding clear instructional comments, and generating a complete markdown tutorial",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "create-architectural-decision-record": {
        "title": "Create Architectural Decision Record",
        "description": "Create an Architectural Decision Record (ADR) document for AI-optimized decision documentation",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "create-github-issue-feature-from-specification": {
        "title": "Create GitHub Issue from Specification",
        "description": "Create GitHub Issue for feature request from specification file using feature_request.yml template",
        "category": "project-management",
        "tools": ["changes", "codebase", "editFiles", "githubRepo", "problems"]
    },
    "create-github-issues-feature-from-implementation-plan": {
        "title": "Create GitHub Issue from Implementation Plan",
        "description": "Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates",
        "category": "project-management",
        "tools": ["changes", "codebase", "editFiles", "githubRepo", "problems"]
    },
    "create-github-issues-for-unmet-specification-requirements": {
        "title": "Create GitHub Issues for Unmet Specification Requirements",
        "description": "Create GitHub Issues for unimplemented requirements from specification files using feature_request.yml template",
        "category": "project-management",
        "tools": ["changes", "codebase", "editFiles", "githubRepo", "problems"]
    },
    "create-implementation-plan": {
        "title": "Create Implementation Plan",
        "description": "Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design, architecture or infrastructure",
        "category": "planning",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "create-llms": {
        "title": "Create LLMs.txt File from Repository Structure",
        "description": "Create an llms.txt file from scratch based on repository structure following the llms.txt specification at https://llmstxt.org/",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "create-oo-component-documentation": {
        "title": "Generate Standard OO Component Documentation",
        "description": "Create comprehensive, standardized documentation for object-oriented components following industry best practices and architectural documentation standards",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "create-specification": {
        "title": "Create Specification",
        "description": "Create a new specification file for the solution, optimized for Generative AI consumption",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "create-spring-boot-java-project": {
        "title": "Create Spring Boot Java project prompt",
        "description": "Create Spring Boot Java project skeleton",
        "category": "development",
        "tools": ["changes", "codebase", "editFiles", "findTestFiles", "problems", "runCommands", "runTests", "search", "searchResults", "terminalLastCommand", "testFailure", "usages"]
    },
    "create-spring-boot-kotlin-project": {
        "title": "Create Spring Boot Kotlin project prompt",
        "description": "Create Spring Boot Kotlin project skeleton",
        "category": "development",
        "tools": ["changes", "codebase", "editFiles", "findTestFiles", "problems", "runCommands", "runTests", "search", "searchResults", "terminalLastCommand", "testFailure", "usages"]
    },
    "csharp-async": {
        "title": "C# Async Programming Best Practices",
        "description": "Get best practices for C# async programming",
        "category": "best-practices",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "csharp-docs": {
        "title": "C# Documentation Best Practices",
        "description": "Ensure that C# types are documented with XML comments and follow best practices for documentation",
        "category": "best-practices",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "csharp-mstest": {
        "title": "MSTest Best Practices",
        "description": "Get best practices for MSTest unit testing, including data-driven tests",
        "category": "testing",
        "tools": ["changes", "codebase", "editFiles", "problems", "search"]
    },
    "csharp-nunit": {
        "title": "NUnit Best Practices",
        "description": "Get best practices for NUnit unit testing, including data-driven tests",
        "category": "testing",
        "tools": ["changes", "codebase", "editFiles", "problems", "search"]
    },
    "csharp-xunit": {
        "title": "XUnit Best Practices",
        "description": "Get best practices for XUnit unit testing, including data-driven tests",
        "category": "testing",
        "tools": ["changes", "codebase", "editFiles", "problems", "search"]
    },
    "dotnet-best-practices": {
        "title": ".NET/C# Best Practices",
        "description": "Ensure .NET/C# code meets best practices for the solution/project",
        "category": "best-practices",
        "tools": []
    },
    "dotnet-design-pattern-review": {
        "title": ".NET/C# Design Pattern Review",
        "description": "Review the C#/.NET code for design pattern implementation and suggest improvements",
        "category": "code-review",
        "tools": []
    },
    "ef-core": {
        "title": "Entity Framework Core Best Practices",
        "description": "Get best practices for Entity Framework Core",
        "category": "best-practices",
        "tools": ["changes", "codebase", "editFiles", "problems", "runCommands"]
    },
    "gen-specs-as-issues": {
        "title": "Product Manager Assistant: Feature Identification and Specification",
        "description": "This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation",
        "category": "project-management",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "javascript-typescript-jest": {
        "title": "Javascript Typescript Jest",
        "description": "Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns",
        "category": "testing",
        "tools": []
    },
    "multi-stage-dockerfile": {
        "title": "Multi Stage Dockerfile",
        "description": "Create optimized multi-stage Dockerfiles for any language or framework",
        "category": "devops",
        "tools": ["codebase"]
    },
    "my-issues": {
        "title": "My Issues",
        "description": "List my issues in the current repository",
        "category": "github",
        "tools": ["githubRepo", "github", "get_issue", "get_issue_comments", "get_me", "list_issues"]
    },
    "my-pull-requests": {
        "title": "My Pull Requests",
        "description": "List my pull requests in the current repository",
        "category": "github",
        "tools": ["githubRepo", "github", "get_me", "get_pull_request", "get_pull_request_comments", "get_pull_request_diff", "get_pull_request_files", "get_pull_request_reviews", "get_pull_request_status", "list_pull_requests", "request_copilot_review"]
    },
    "next-intl-add-language": {
        "title": "Next Intl Add Language",
        "description": "Add new language to a Next.js + next-intl application",
        "category": "development",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "suggest-awesome-github-copilot-chatmodes": {
        "title": "Suggest Awesome GitHub Copilot Chatmodes",
        "description": "Suggest relevant GitHub Copilot chatmode files from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing chatmodes in this repository",
        "category": "meta",
        "tools": ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
    },
    "suggest-awesome-github-copilot-prompts": {
        "title": "Suggest Awesome GitHub Copilot Prompts",
        "description": "Suggest relevant GitHub Copilot prompt files from the awesome-copilot repository based on current repository context and chat history, avoiding duplicates with existing prompts in this repository",
        "category": "meta",
        "tools": ["changes", "codebase", "editFiles", "fetch", "findTestFiles", "githubRepo", "new", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI", "github"]
    },
    "update-avm-modules-in-bicep": {
        "title": "Update Azure Verified Modules in Bicep Files",
        "description": "Update Azure Verified Modules (AVM) to latest versions in Bicep files",
        "category": "cloud",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    },
    "update-implementation-plan": {
        "title": "Update Implementation Plan",
        "description": "Update an existing implementation plan file with new or update requirements to provide new features, refactoring existing code or upgrading packages, design, architecture or infrastructure",
        "category": "planning",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "update-llms": {
        "title": "Update LLMs.txt File",
        "description": "Update the llms.txt file in the root folder to reflect changes in documentation or specifications following the llms.txt specification at https://llmstxt.org/",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "update-markdown-file-index": {
        "title": "Update Markdown File Index",
        "description": "Update a markdown file section with an index/table of files from a specified folder",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "findTestFiles", "githubRepo", "openSimpleBrowser", "problems", "runCommands", "runTasks", "runTests", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "update-oo-component-documentation": {
        "title": "Update Standard OO Component Documentation",
        "description": "Update existing object-oriented component documentation following industry best practices and architectural documentation standards",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "extensions", "fetch", "githubRepo", "openSimpleBrowser", "problems", "runTasks", "search", "searchResults", "terminalLastCommand", "terminalSelection", "testFailure", "usages", "vscodeAPI"]
    },
    "update-specification": {
        "title": "Update Specification",
        "description": "Update an existing specification file for the solution, optimized for Generative AI consumption based on new requirements or updates to any existing code",
        "category": "documentation",
        "tools": ["changes", "codebase", "editFiles", "problems"]
    }
}

# Resources for exposing prompt metadata and content
@mcp.resource("copilot-prompts://list")
def list_all_prompts() -> str:
    """Get a list of all available GitHub Copilot prompts."""
    prompts_info = []
    for prompt_id, metadata in PROMPTS_REGISTRY.items():
        prompts_info.append({
            "id": prompt_id,
            "title": metadata["title"],
            "description": metadata["description"],
            "category": metadata["category"],
            "url": f"https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md"
        })
    
    return json.dumps(prompts_info, indent=2)

@mcp.resource("copilot-prompts://categories")
def list_prompt_categories() -> str:
    """Get all prompt categories and their counts."""
    categories = {}
    for metadata in PROMPTS_REGISTRY.values():
        category = metadata["category"]
        categories[category] = categories.get(category, 0) + 1
    
    return json.dumps(categories, indent=2)

@mcp.resource("copilot-prompts://{category}")
def get_prompts_by_category(category: str) -> str:
    """Get all prompts in a specific category."""
    filtered_prompts = []
    for prompt_id, metadata in PROMPTS_REGISTRY.items():
        if metadata["category"] == category:
            filtered_prompts.append({
                "id": prompt_id,
                "title": metadata["title"],
                "description": metadata["description"],
                "tools": metadata["tools"],
                "url": f"https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md"
            })
    
    return json.dumps(filtered_prompts, indent=2)

@mcp.resource("copilot-prompts://prompt/{prompt_id}")
def get_prompt_details(prompt_id: str) -> str:
    """Get detailed information about a specific prompt."""
    if prompt_id not in PROMPTS_REGISTRY:
        return json.dumps({"error": f"Prompt '{prompt_id}' not found"})
    
    metadata = PROMPTS_REGISTRY[prompt_id]
    details = {
        "id": prompt_id,
        "title": metadata["title"],
        "description": metadata["description"],
        "category": metadata["category"],
        "tools": metadata["tools"],
        "url": f"https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md",
        "install_url": f"https://vscode.dev/redirect?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2F{prompt_id}.prompt.md"
    }
    
    return json.dumps(details, indent=2)

# Tools for working with prompts
@mcp.tool()
def search_prompts(query: str, category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Search for prompts by title, description, or category.
    
    Args:
        query: Search query to match against title and description
        category: Optional category filter
    
    Returns:
        List of matching prompts with their metadata
    """
    results = []
    query_lower = query.lower()
    
    for prompt_id, metadata in PROMPTS_REGISTRY.items():
        # Filter by category if specified
        if category and metadata["category"] != category:
            continue
        
        # Search in title and description
        if (query_lower in metadata["title"].lower() or 
            query_lower in metadata["description"].lower() or
            query_lower in metadata["category"].lower()):
            
            results.append({
                "id": prompt_id,
                "title": metadata["title"],
                "description": metadata["description"],
                "category": metadata["category"],
                "tools": metadata["tools"],
                "url": f"https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md"
            })
    
    return results

@mcp.tool()
def get_prompt_installation_instructions(prompt_id: str) -> Dict[str, Any]:
    """
    Get installation instructions for a specific prompt.
    
    Args:
        prompt_id: The ID of the prompt to get installation instructions for
    
    Returns:
        Installation instructions and URLs
    """
    if prompt_id not in PROMPTS_REGISTRY:
        return {"error": f"Prompt '{prompt_id}' not found"}
    
    metadata = PROMPTS_REGISTRY[prompt_id]
    
    return {
        "prompt_id": prompt_id,
        "title": metadata["title"],
        "description": metadata["description"],
        "installation": {
            "vscode": f"https://vscode.dev/redirect?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2F{prompt_id}.prompt.md",
            "vscode_insiders": f"https://insiders.vscode.dev/redirect?url=vscode-insiders%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2F{prompt_id}.prompt.md",
            "raw_url": f"https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/{prompt_id}.prompt.md"
        },
        "usage_instructions": [
            f"Use `/{prompt_id}` in VS Code chat",
            "Run `Chat: Run Prompt` command",
            "Hit the run button while you have a prompt open"
        ]
    }

@mcp.tool()
def get_prompts_by_tools(required_tools: List[str]) -> List[Dict[str, Any]]:
    """
    Find prompts that use specific tools.
    
    Args:
        required_tools: List of tools that the prompts should support
    
    Returns:
        List of prompts that use the specified tools
    """
    results = []
    
    for prompt_id, metadata in PROMPTS_REGISTRY.items():
        prompt_tools = set(metadata["tools"])
        required_tools_set = set(required_tools)
        
        # Check if all required tools are supported by this prompt
        if required_tools_set.issubset(prompt_tools):
            results.append({
                "id": prompt_id,
                "title": metadata["title"],
                "description": metadata["description"],
                "category": metadata["category"],
                "tools": metadata["tools"],
                "matching_tools": list(required_tools_set.intersection(prompt_tools)),
                "url": f"https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md"
            })
    
    return results

@mcp.tool()
def generate_prompt_usage_guide(category: Optional[str] = None) -> str:
    """
    Generate a comprehensive usage guide for prompts.
    
    Args:
        category: Optional category to filter prompts
    
    Returns:
        Markdown formatted usage guide
    """
    guide_lines = [
        "# Awesome GitHub Copilot Prompts Usage Guide",
        "",
        "This guide provides information about available GitHub Copilot prompts from the awesome-copilot repository.",
        ""
    ]
    
    # Group prompts by category
    categories = {}
    for prompt_id, metadata in PROMPTS_REGISTRY.items():
        if category and metadata["category"] != category:
            continue
        
        cat = metadata["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((prompt_id, metadata))
    
    # Generate guide content
    for cat, prompts in sorted(categories.items()):
        guide_lines.extend([
            f"## {cat.title()} Prompts",
            ""
        ])
        
        for prompt_id, metadata in sorted(prompts, key=lambda x: x[1]["title"]):
            guide_lines.extend([
                f"### {metadata['title']}",
                f"**ID:** `{prompt_id}`",
                f"**Description:** {metadata['description']}",
                ""
            ])
            
            if metadata["tools"]:
                guide_lines.extend([
                    "**Required Tools:**",
                    ", ".join(f"`{tool}`" for tool in metadata["tools"]),
                    ""
                ])
            
            guide_lines.extend([
                "**Installation:**",
                f"- [Install in VS Code](https://vscode.dev/redirect?url=vscode%3Achat-prompt%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Fgithub%2Fawesome-copilot%2Fmain%2Fprompts%2F{prompt_id}.prompt.md)",
                f"- [View Source](https://github.com/github/awesome-copilot/blob/main/prompts/{prompt_id}.prompt.md)",
                "",
                "**Usage:**",
                f"Use `/{prompt_id}` in VS Code chat or run the `Chat: Run Prompt` command.",
                "",
                "---",
                ""
            ])
    
    guide_lines.extend([
        "## General Usage Instructions",
        "",
        "1. **Install a prompt:** Click the installation link for any prompt above",
        "2. **Use in VS Code:** Type `/prompt-name` in the chat interface",
        "3. **Run command:** Use `Chat: Run Prompt` command from the command palette",
        "4. **Direct execution:** Hit the run button while viewing a prompt file",
        "",
        "For more information, visit the [awesome-copilot repository](https://github.com/github/awesome-copilot)."
    ])
    
    return "\n".join(guide_lines)

# Prompts for common workflows
@mcp.prompt(title="Find Development Prompts")
def find_development_prompts(language: str = "any", framework: str = "any") -> str:
    """Find development-related prompts for specific languages or frameworks."""
    return f"""Find GitHub Copilot prompts suitable for {language} development with {framework} framework.

Use the search_prompts tool to find relevant prompts in the "development", "best-practices", and "testing" categories.

Consider prompts that might help with:
- Project scaffolding and setup
- Best practices and code quality
- Testing frameworks and patterns
- Documentation generation
- Code review and refactoring

Provide installation instructions and usage examples for the most relevant prompts."""

@mcp.prompt(title="Setup GitHub Workflow Prompts")
def setup_github_workflow_prompts() -> str:
    """Find prompts for GitHub workflow automation and project management."""
    return """Find GitHub Copilot prompts that help with GitHub workflows and project management.

Search for prompts in the "github" and "project-management" categories that can help with:
- Creating and managing GitHub issues
- Pull request workflows
- Implementation planning
- Specification documentation
- Project organization

Provide a curated list with installation instructions and explain how these prompts can streamline GitHub workflows."""

@mcp.prompt(title="Documentation Prompts Setup")
def documentation_prompts_setup() -> str:
    """Find and recommend documentation-related prompts."""
    return """Find GitHub Copilot prompts that help with documentation tasks.

Search for prompts in the "documentation" category and recommend the best ones for:
- API documentation
- Code documentation
- Project specifications
- Architectural decisions
- Component documentation
- README and guide generation

Provide installation instructions and examples of when to use each prompt type."""

if __name__ == "__main__":
    mcp.run()
