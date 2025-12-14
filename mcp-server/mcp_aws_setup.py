import json
import os

from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session

from aws_utils import setup_cognito_user_pool

boto_session = Session()
region = boto_session.region_name

ssm_client = boto_session.client('ssm', region_name=region)
secrets_client = boto_session.client('secretsmanager', region_name=region)
agentcore_control_client = boto_session.client("bedrock-agentcore-control", region_name=region)

tool_name = "mcp_server_agentcore"


def configure_cognito_user_pool():
    print("Setting up Amazon Cognito user pool...")
    print(f"Using AWS region: {region}")
    cognito_config = setup_cognito_user_pool()
    print("Cognito setup completed ✓")
    print(f"User Pool ID: {cognito_config.get('pool_id', 'N/A')}")
    print(f"Client ID: {cognito_config.get('client_id', 'N/A')}")

    return cognito_config


def store_cognito_credentials(cognito_config):
    try:
        secrets_client.create_secret(
            Name='mcp_server/cognito/credentials',
            Description='Cognito credentials for MCP server',
            SecretString=json.dumps(cognito_config)
        )
        print("✓ Cognito credentials stored in Secrets Manager")
    except secrets_client.exceptions.ResourceExistsException:
        secrets_client.update_secret(
            SecretId='mcp_server/cognito/credentials',
            SecretString=json.dumps(cognito_config)
        )
        print("✓ Cognito credentials updated in Secrets Manager")


def configure_agentcore_runtime(cognito_config):
    required_files = ['mcp_server.py', 'requirements.txt']
    for file in required_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Required file {file} not found")
    print("All required files found ✓")

    agentcore_runtime = Runtime()

    auth_config = {
        "customJWTAuthorizer": {
            "allowedClients": [
                cognito_config['client_id']
            ],
            "discoveryUrl": cognito_config['discovery_url'],
        }
    }

    print("Configuring AgentCore Runtime...")
    agentcore_runtime.configure(
        entrypoint="mcp_server.py",
        auto_create_execution_role=True,
        auto_create_ecr=True,
        requirements_file="requirements.txt",
        region=region,
        authorizer_configuration=auth_config,
        protocol="MCP",
        agent_name=tool_name
    )
    print("Configuration completed ✓")

    return agentcore_runtime


def launch_agentcore_runtime(agentcore_runtime):
    print("Launching MCP server to AgentCore Runtime...")
    print("This may take several minutes...")
    launch_result = agentcore_runtime.launch()
    print("Launch completed ✓")
    print(f"Agent ARN: {launch_result.agent_arn}")
    print(f"Agent ID: {launch_result.agent_id}")

    return launch_result


def store_agent_arn(launch_result):
    ssm_client.put_parameter(
        Name='/mcp_server/runtime/agent_arn',
        Value=launch_result.agent_arn,
        Type='String',
        Description='Agent ARN for MCP server',
        Overwrite=True
    )
    print("✓ Agent ARN stored in Parameter Store")

    print("\nConfiguration stored successfully!")
    print(f"Agent ARN: {launch_result.agent_arn}")


def main():
    cognito_config = configure_cognito_user_pool()
    store_cognito_credentials(cognito_config)
    agentcore_runtime = configure_agentcore_runtime(cognito_config)
    launch_result = launch_agentcore_runtime(agentcore_runtime)
    store_agent_arn(launch_result)


if __name__ == "__main__":
    main()
