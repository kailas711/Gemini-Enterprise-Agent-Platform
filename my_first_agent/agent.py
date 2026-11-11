from google.adk.agents import Agent, LlmAgent 
from google.adk.tools import google_search
from google.genai import types

# Multi-agent system with 2 agents
root_agent = Agent(
    model="gemini-3-flash-preview",
    name="billing_agent",
    # OTHER agents read this to decide if they should delegate here
    description="Handles customer billing inquiries and payment processing",
    # THIS agent reads this to know how to behave
    instruction="""You are a billing specialist.

    When helping customers:
    1. Be empathetic and patient
    2. Explain charges clearly
    3. Use the billing_lookup tool to check account details
    4. Never promise refunds without manager approval

    Always maintain a professional, helpful tone.""",
    tools=[google_search]
)