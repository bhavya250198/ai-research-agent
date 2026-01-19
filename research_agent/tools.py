from datetime import datetime
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool


def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Append structured research text to a timestamped file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)

    return f"Data successfully saved to {filename}"


SAVE_TOOL = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save structured research data to a text file.",
)

_search = DuckDuckGoSearchRun()
SEARCH_TOOL = Tool(
    name="search",
    func=_search.run,
    description="Search the web for information.",
)

_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
WIKI_TOOL = WikipediaQueryRun(api_wrapper=_api_wrapper)

