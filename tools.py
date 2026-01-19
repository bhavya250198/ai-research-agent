"""
Backwards-compatible re-exports for tools.
The canonical implementations live in research_agent.tools.
"""

from research_agent.tools import SAVE_TOOL as save_tool
from research_agent.tools import SEARCH_TOOL as search_tool
from research_agent.tools import WIKI_TOOL as wiki_tool

__all__ = ["save_tool", "search_tool", "wiki_tool"]