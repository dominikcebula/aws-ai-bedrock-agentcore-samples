from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator  # Import the calculator tool

app = BedrockAgentCoreApp()


@tool
def weather():
    """ Get weather """  # Dummy implementation
    return "sunny"


model_id = "meta.llama3-2-1b-instruct-v1:0"
model = BedrockModel(
    model_id=model_id,
)
agent = Agent(
    model=model,
    tools=[calculator, weather],
    system_prompt="You're a helpful assistant. You can do simple math calculation, and tell the weather."
)


@app.entrypoint
def strands_agent_bedrock(payload):
    user_input = payload.get("prompt")
    print("User input:", user_input)
    response = agent(user_input)
    return response.message['content'][0]['text']


if __name__ == "__main__":
    app.run()
