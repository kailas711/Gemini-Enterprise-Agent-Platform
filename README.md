# Gemini Enterprise Agent Platform

This repository is a lightweight starter project for learning how to build agentic applications with Google AI tooling and the Google Agent Development Kit (ADK). It is intentionally simple, so you can extend it as you study agent patterns, tool use, orchestration, and workflow design.

It is designed to support a hands-on learning path inspired by the Google Developers GEAR program: https://developers.google.com/program/gear

## Why this repository exists

The goal of this project is to give you a clean starting point for experimenting with:

- LLM-powered agents
- Simple agent definitions and instructions
- Model configuration and environment variables
- Multi-step agentic workflows
- Tool integration and orchestration
- Secure handling of API keys and credentials

This repository is intentionally minimal, so it is easy to understand and easy to expand.

## Repository structure

```text
Gemini-Enterprise-Agent-Platform/
├── README.md
├── my_first_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env
└── .gitignore
```

### `my_first_agent/agent.py`
This file defines a minimal AI agent using Google ADK:

- `Gemini(model="gemma-4-26b-a4b-it")` selects the model
- `Agent(...)` creates the agent
- `instruction` defines the behavior of the assistant
- `root_agent` is the entry point for the application

## Current starter agent

The repo currently contains a very basic agent:

```python
from google.adk.models import Gemini
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model=Gemini(model="gemma-4-26b-a4b-it"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```

This is a good starting point for learning how a model, agent wrapper, and instruction prompt work together.

## Getting started

### 1. Prerequisites

Make sure you have:

- Python 3.10+ recommended
- Access to a Google AI / Gemini API key
- A virtual environment for experiments and local learning

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.\.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install the Google Agent Development Kit and any required packages for your environment:

```bash
pip install google-adk
```

If you use additional packages for environment management or app development, install them as needed.

### 4. Configure your API key

The project includes a `.env` file for local configuration. Keep your keys out of source control.

Example:

```env
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=your_api_key_here
```

The repository's `.gitignore` is already configured to ignore `.env` and `.adk/` local state.

## Running the agent

This repository is a foundation for a local agent runner or notebook. You can verify the package imports correctly with:

```bash
python -c "from my_first_agent.agent import root_agent; print(root_agent.name, root_agent.description)"
```

This does not execute an app server, but it confirms the agent is defined correctly and ready to be connected to a runner or orchestration layer.

## Recommended learning path

Following the GEAR spirit, use this project as a sandbox for iterative learning:

### Phase 1: Learn the basics
- Understand the request → model → response loop
- Experiment with system prompts and user instructions
- Change the `instruction` text and observe how behavior changes

### Phase 2: Add structure
- Split logic into tools and helper functions
- Create specialized agents for tasks like research, writing, and decision support
- Add memory or session state for context retention

### Phase 3: Build workflows
- Chain agents together in a workflow
- Create a planner agent and worker agents
- Add task routing and tool selection

### Phase 4: Add evaluation and safety
- Validate outputs against quality criteria
- Add clear instructions and guardrails
- Handle failures and edge cases

### Phase 5: Production thinking
- Use environment variables for secrets
- Keep code modular and testable
- Design for logging, auditing, and observability

## Suggested next improvements

As you grow the project, these are good next steps:

- Add a real app entrypoint (CLI, web app, or FastAPI service)
- Add tool calling for web search, file access, or external APIs
- Create multiple specialized agents instead of a single `root_agent`
- Add a workflow layer that orchestrates tasks across agents
- Store conversation history or memory in a local database
- Add tests for agent behavior and workflow reliability

## Security notes

When building AI apps:

- Never commit API keys or secrets
- Keep `.env` files local and ignored by git
- Validate inputs before sending them to external tools
- Be careful with tool permissions and external actions
- Treat model outputs as untrusted until verified

## Learning prompt ideas

Try these experiments as you learn:

1. Change the agent instruction to be more specific
2. Ask the agent to act as a researcher, tutor, or software engineer
3. Add a tool that fetches data from an API
4. Create a workflow with a planner agent and executor agent
5. Add a memory layer for short-term context

## Notes

This repository is intentionally simple to help you focus on the fundamentals of agentic design rather than framework complexity.

You can use it as a foundation for:

- learning agent architecture
- prototyping agent workflows
- testing ideas before scaling to larger systems
- exploring Google’s AI ecosystem and agent patterns

## References

- Google Developers GEAR program: https://developers.google.com/program/gear
- Google Agent Development Kit: https://developers.google.com/ai

## License

This project does not yet include a formal license file. If you plan to share or build on top of it publicly, add a license that matches your intended usage.

---

This repository is best treated as a learning sandbox. Start small, inspect the agent definition, test changes carefully, and build one useful workflow at a time.
