# MCP Best Practices: Creating a Jira Ticket via MCP Tools

This document outlines the recommended steps and setups for creating a Jira ticket using MCP (Model Context Protocol) tools, based on a real-world workflow.

---

## 1. Gather Required Information

- **Project Key** (e.g., `DASD`)
- **Issue Type** (e.g., `Task`, `DASD: Data Governance`)
- **Summary** (Title)
- **Description** (Body)
- **Assignee** (optional)
- **Any required custom fields** (e.g., `customfield_10900` for request type)

---

## 2. Check Required Fields

- Use the MCP tool `jira_search_fields` to list all fields for the project.
- If ticket creation fails, inspect required custom fields by examining recent issues with `jira_search` (use `fields: "*all"`).
- Identify any fields that must be set (e.g., request type, delivery quarter, etc.).

---

## 3. Create the Simplest Ticket

- Use the `jira_create_issue` tool with only the required fields.
- If creation fails, incrementally add placeholder values for required custom fields.

**Example:**
```json
{
  "project_key": "DASD",
  "summary": "Add external locations to workspaces – placeholder",
  "issue_type": "DASD: Data Governance",
  "description": "",
  "assignee": "",
  "additional_fields": {
    "customfield_10900": "111" // Placeholder for request type
  }
}
```

---

## 4. Update Title and Description

- Use the `jira_update_issue` tool to set the final summary and description.

**Example:**
```json
{
  "issue_key": "DASD-6290",
  "fields": {
    "summary": "Request external locations for ai-databricks-output buckets",
    "description": "Hello team,\n\nHow do I request a new external location to be added on my team’s workspace?\n\nThe buckets already exist; we just need the external locations added as we do not have permissions.\n\n**Buckets:**\n• s3://ai-databricks-output-production\n• s3://ai-databricks-output-staging\n\n**AWS Account:** 121314186679\n\n**Workspaces:**\n• https://compass-ai-prod.cloud.databricks.com/\n• https://compass-ai-gamma.cloud.databricks.com/\n\nThank you,\nGastón Barbero :tadaco:"
  }
}
```

---

## 5. Verify and Finalize

- Confirm the ticket is created and visible in Jira.
- Add or update any additional fields as needed via the Jira UI or MCP tools.

---

## 6. Troubleshooting

- If ticket creation fails:
  - Double-check required fields for the issue type and project.
  - Use `jira_search_fields` and `jira_search` to inspect field requirements and recent tickets.
  - Try using a different issue type if the default one fails.
  - Add placeholder values for custom fields as needed.

---

## Example MCP Tool Calls

### Create Issue

```json
{
  "tool": "jira_create_issue",
  "arguments": {
    "project_key": "DASD",
    "summary": "Add external locations to workspaces – placeholder",
    "issue_type": "DASD: Data Governance",
    "description": "",
    "assignee": "",
    "additional_fields": {
      "customfield_10900": "111"
    }
  }
}
```

### Update Issue

```json
{
  "tool": "jira_update_issue",
  "arguments": {
    "issue_key": "DASD-6290",
    "fields": {
      "summary": "Request external locations for ai-databricks-output buckets",
      "description": "Hello team,\n\nHow do I request a new external location to be added on my team’s workspace?\n\nThe buckets already exist; we just need the external locations added as we do not have permissions.\n\n**Buckets:**\n• s3://ai-databricks-output-production\n• s3://ai-databricks-output-staging\n\n**AWS Account:** 121314186679\n\n**Workspaces:**\n• https://compass-ai-prod.cloud.databricks.com/\n• https://compass-ai-gamma.cloud.databricks.com/\n\nThank you,\nGastón Barbero :tadaco:"
    }
  }
}
```

---

## Summary

- Always start with the minimum required fields.
- Use MCP tools to inspect and troubleshoot field requirements.
- Update the ticket after creation for clarity and completeness.
- Document your steps for reproducibility and team knowledge sharing.