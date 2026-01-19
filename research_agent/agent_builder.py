from __future__ import annotations

from typing import Iterable, Optional, Any
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate


def build_agent_executor(
    llm: BaseChatModel,
    prompt: ChatPromptTemplate,
    tools: Iterable[Any],
    verbose: bool = True,
) -> AgentExecutor:
    """Wire the LLM, prompt, and tools into a LangChain AgentExecutor."""

    agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
    return AgentExecutor(agent=agent, tools=tools, verbose=verbose)


def parse_structured_output(
    raw_response: Any, parser: PydanticOutputParser
) -> Optional[Any]:
    """Attempt to parse the agent output into the structured schema."""

    candidate_text: Optional[str] = None

    if isinstance(raw_response, dict):
        if isinstance(raw_response.get("output"), str):
            candidate_text = raw_response["output"]
        elif isinstance(raw_response.get("output"), list) and raw_response["output"]:
            first = raw_response["output"][0]
            if isinstance(first, dict) and "text" in first:
                candidate_text = first["text"]

    if not candidate_text:
        return None

    try:
        return parser.parse(candidate_text)
    except Exception:
        return None

