from pathlib import Path

from bedrock_agentcore_starter_toolkit.operations.runtime import destroy_bedrock_agentcore
from boto3.session import Session

boto_session = Session()
region = boto_session.region_name

ssm_client = boto_session.client('ssm', region_name=region)
secrets_client = boto_session.client('secretsmanager', region_name=region)
agentcore_control_client = boto_session.client("bedrock-agentcore-control", region_name=region)

tool_name = "mcp_server_agentcore"


def cleanup():
    print("🗑️  Starting cleanup process...")

    try:
        ssm_client.delete_parameter(Name='/mcp_server/runtime/agent_arn')
        print("✓ Parameter Store parameter deleted")
    except ssm_client.exceptions.ParameterNotFound:
        print("ℹ️  Parameter Store parameter not found")

    try:
        secrets_client.delete_secret(
            SecretId='mcp_server/cognito/credentials',
            ForceDeleteWithoutRecovery=True
        )
        print("✓ Secrets Manager secret deleted")
    except secrets_client.exceptions.ResourceNotFoundException:
        print("ℹ️  Secrets Manager secret not found")

    destroy_bedrock_agentcore(
        config_path=Path(".bedrock_agentcore.yaml"),
        agent_name=tool_name,
        delete_ecr_repo=True
    )

    print("\n✅ Cleanup completed successfully!")


if __name__ == "__main__":
    cleanup()
