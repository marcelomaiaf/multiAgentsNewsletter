from agents import Agent, WebSearchTool
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

from prompts.instructions import instructions_coletor
from tools.agents_tools import buscar_noticias, get_extrator_tool

coletor = Agent(
    name="coletor",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} {instructions_coletor}",
    model="gpt-4.1-mini-2025-04-14",
    tools=[WebSearchTool(), buscar_noticias, get_extrator_tool()]
)
