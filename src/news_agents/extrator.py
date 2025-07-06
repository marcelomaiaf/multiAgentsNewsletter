from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

from prompts.instructions import instructions_extrator
from tools.agents_tools import crawler

extrator = Agent(
    name="extrator",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} {instructions_extrator}",
    model="gpt-4.1-mini-2025-04-14",
    tools=[crawler]
)