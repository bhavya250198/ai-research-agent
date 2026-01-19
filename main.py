from dotenv import load_dotenv

from research_agent import (
    SAVE_TOOL,
    SEARCH_TOOL,
    WIKI_TOOL,
    build_agent_executor,
    build_prompt,
    create_parser,
    get_anthropic_llm,
    parse_structured_output,
)


def main() -> None:
    """Run a simple CLI loop for the research assistant."""

    load_dotenv(override=True)

    llm = get_anthropic_llm()
    parser = create_parser()
    prompt = build_prompt(parser)
    tools = [SEARCH_TOOL, WIKI_TOOL, SAVE_TOOL]

    agent_executor = build_agent_executor(
        llm=llm, prompt=prompt, tools=tools, verbose=True
    )

    user_query = input("How may I help you? ")
    raw_response = agent_executor.invoke({"query": user_query})
    print(raw_response)

    structured = parse_structured_output(raw_response, parser)
    if structured:
        print("Structured Response", structured)
    else:
        print("Structured response unavailable; see raw output above.")


if __name__ == "__main__":
    main()