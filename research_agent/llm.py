from langchain_anthropic import ChatAnthropic


def get_anthropic_llm(
    model: str = "claude-3-haiku-20240307", temperature: float = 0.3
) -> ChatAnthropic:
    """Return a configured Anthropic chat model for the agent."""

    return ChatAnthropic(model=model, temperature=temperature)

