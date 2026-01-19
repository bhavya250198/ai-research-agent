"""
Research agent package that encapsulates the LangChain-based assistant.
Exposes factories for the LLM, prompt, schema, tools, and agent executor.
"""

from .llm import get_anthropic_llm
from .schema import ResearchResponse, create_parser
from .prompting import build_prompt
from .tools import SAVE_TOOL, SEARCH_TOOL, WIKI_TOOL
from .agent_builder import build_agent_executor, parse_structured_output

__all__ = [
    "get_anthropic_llm",
    "ResearchResponse",
    "create_parser",
    "build_prompt",
    "SAVE_TOOL",
    "SEARCH_TOOL",
    "WIKI_TOOL",
    "build_agent_executor",
    "parse_structured_output",
]

