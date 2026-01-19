AI Research Agent
=================

Lightweight CLI research assistant built with LangChain and Anthropic Claude. The agent can search the web (DuckDuckGo), query Wikipedia, and save structured results to a local file.

Features
--------
- Tool-calling agent powered by Anthropic Claude (`ChatAnthropic`).
- Web search via DuckDuckGo and Wikipedia lookup.
- Structured responses validated with Pydantic schema.
- Optional save-to-file tool that appends results with timestamps.

Quickstart
----------
1) Install dependencies (recommended: inside a virtualenv):
```
pip install -r requirements.txt
```

2) Set environment variables (create `.env`):
```
ANTHROPIC_API_KEY=your_key_here
```

3) Run the CLI:
```
python main.py
```
Enter a research question when prompted; the agent may call search/wiki tools and will print both raw and structured outputs.

Project Structure
-----------------
- `main.py` – CLI entrypoint that wires the LLM, prompt, tools, and schema.
- `research_agent/agent_builder.py` – Agent executor wiring and structured output parser.
- `research_agent/prompting.py` – System prompt template with format instructions injection.
- `research_agent/schema.py` – `ResearchResponse` Pydantic model + parser factory.
- `research_agent/llm.py` – Anthropic LLM factory (`claude-3-haiku-20240307`, temp 0.3).
- `research_agent/tools.py` – DuckDuckGo search, Wikipedia query, and save-to-file tool.
- `utilities/api_key_validation.py` – Helper to validate `ANTHROPIC_API_KEY`.

Configuration
-------------
- Default model: `claude-3-haiku-20240307`; adjust in `research_agent/llm.py` if needed.
- Output file for saves: `research_output.txt` (appends, timestamped).
- Wikipedia tool limits: `top_k_results=1`, `doc_content_chars_max=100` (tune in `tools.py`).

Extending
---------
- Add new tools in `research_agent/tools.py` and include them in the `tools` list in `main.py`.
- Update `ResearchResponse` (schema.py) and the prompt (prompting.py) if you need different structured outputs.
- For other LLMs/providers, swap the factory in `llm.py` and pass the new model into `main.py`.

Troubleshooting
---------------
- Ensure `ANTHROPIC_API_KEY` is set and valid (see `utilities/api_key_validation.py` for a check).
- If searches fail, confirm network access and that DuckDuckGo/Wikipedia dependencies are installed.


