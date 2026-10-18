from google.adk.models import Gemini
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model=Gemini(model="gemma-4-26b-a4b-it"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
