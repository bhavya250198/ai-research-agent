from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser


class ResearchResponse(BaseModel):
    """Structured research result returned by the agent."""

    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


def create_parser() -> PydanticOutputParser:
    """Create a parser that enforces the ResearchResponse schema."""

    return PydanticOutputParser(pydantic_object=ResearchResponse)

