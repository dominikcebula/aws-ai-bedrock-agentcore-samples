# 📦 MCP Server on AWS AgentCore Runtime

## 📝 Overview

This repository contains a sample code for MCP Server running on the AWS AgentCore Runtime. It exposes basic
arithmetic tools (add, subtract, multiply, divide) via a FastMCP server and demonstrates integration with AWS services
for authentication and deployment. The repository includes scripts for local and remote client interaction, AWS Cognito
setup, and automated cleanup of resources.

## 🚀 Usage

### 🗺️ Introduction

The repository includes scripts for local and remote usage in AWS.

You can try local usage first, then switch to remote usage.

### ⚙️ Requirements

- Python 3.10+
- AWS credentials configured
- Docker

### ⏳ 0. Prerequisites

- Create venv
    ```bash
    python -m venv .venv
    source venv/bin/activate
    ```
- Install requirements
    ```bash
    pip install -r requirements.txt
    ``` 

### ▶️ 1. Start the MCP Server

- Run locally:
  ```bash
  python mcp_server.py
  ```

### 🖥️ 2. Local Client Example

- List available tools from a running local server:
  ```bash
  python mcp_client_local.py
  ```

### ☁️ 3. AWS Setup

- Provision AWS Cognito, secrets, and AgentCore runtime:
  ```bash
  python mcp_aws_setup.py
  ```

### 🌐 4. Remote Client Example

- Connect to a deployed server on AWS (requires setup):
  ```bash
  python mcp_client_remote.py
  ```

### 🧹 5. Cleanup

- Remove AWS resources and clean up:
  ```bash
  python cleanup.py
  ```

## 📄 Script Descriptions

- **mcp_server.py**: Starts the MCP server and exposes arithmetic tools as API endpoints.
- **mcp_client_local.py**: Connects to a local MCP server, lists available tools.
- **mcp_client_remote.py**: Connects to a remote MCP server on AWS, handles authentication, lists and tests tools.
- **mcp_aws_setup.py**: Sets up AWS Cognito user pool, stores credentials in AWS Secrets Manager, and configures the
  AgentCore runtime.
- **aws_utils.py**: Utility functions for AWS Cognito setup and authentication.
- **cleanup.py**: Cleans up AWS resources and AgentCore runtime.

## 🔗 References

- [Hosting MCP Server on Amazon Bedrock AgentCore Runtime - OAuth Inbound Authentication](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/02-hosting-MCP-server/hosting_mcp_server.ipynb)

## ✍ Author

Dominik Cebula

- https://dominikcebula.com/
- https://blog.dominikcebula.com/
- https://www.udemy.com/user/dominik-cebula/
