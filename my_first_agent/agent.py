from google.adk.agents import Agent, LlmAgent 

# Multi-agent system with 2 agents
billing_agent = Agent(
    model="gemini-flash-latest",
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

    Always maintain a professional, helpful tone."""
)

support_agent = Agent(
    model="gemini-flash-latest",
    name="support_agent",
    description="Handles general customer support questions",
    instruction="""You are a customer support agent.

    If a question is about billing, transfer to the billing_agent.
    Otherwise, help the customer directly."""
)

root_agent = Agent(
    model="gemini-flash-latest",
    name="math_tutor_agent",
    description="Helps students learn algebra by guiding them through problem-solving steps.",
    instruction="You are a patient math tutor. Help students with algebra problems."
)