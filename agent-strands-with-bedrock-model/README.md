# 📦 Strands Agent with Amazon Bedrock model in Amazon Bedrock AgentCore Runtime

## 📝 Overview

This repository contains a sample code for Hosting Strands Agent with Amazon Bedrock model in Amazon Bedrock AgentCore
Runtime.

Agent uses Nova Micro Model with two sample tools attached, one for arithmetic operations and one for getting dummy
weather information.

## 🚀 Usage

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

### ☁️ 1. AWS Setup

- Deploy Agent to AWS:
  ```bash
  python deploy.py
  ```

### 🌐 2. Remote Client Example

- Connect to a deployed agent on AWS, execute prompt and see results:
  ```bash
  python agent_client_remote.py
  ```

### 🧹 3. Cleanup

- Remove AWS resources and clean up:
  ```bash
  python cleanup.py
  ```

## 📄 Script Descriptions



## 🔗 References

- [Hosting Strands Agents with Amazon Bedrock models in Amazon Bedrock AgentCore Runtime](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/01-tutorials/01-AgentCore-runtime/01-hosting-agent/01-strands-with-bedrock-model/runtime_with_strands_and_bedrock_models.ipynb)

## ✍ Author

Dominik Cebula

- https://dominikcebula.com/
- https://blog.dominikcebula.com/
- https://www.udemy.com/user/dominik-cebula/
