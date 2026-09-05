from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemma-4-31b-it',
    name='math_tutor_agent',  # More specific internal name
    description='Helps students learn algebra by guiding them through problemsolving steps.',
    instruction='You are a patient math tutor. Help students with algebra problems.'
)
