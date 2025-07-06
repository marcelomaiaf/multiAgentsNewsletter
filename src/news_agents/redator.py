from agents import Agent, WebSearchTool
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

from prompts.instructions import instructions_redator

redator = Agent(
    name="redator",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} {instructions_redator}",
    model="gpt-4.1-mini-2025-04-14",
    tools=[WebSearchTool()],
    reset_tool_choice = True
)