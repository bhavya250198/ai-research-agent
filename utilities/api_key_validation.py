from __future__ import annotations

import os
from typing import Tuple

from anthropic import Anthropic
from dotenv import load_dotenv


def validate_env_var(name: str) -> Tuple[bool, str]:
    """Check that an environment variable exists and is non-empty."""

    load_dotenv(override=True)
    value = os.getenv(name)
    if not value:
        return False, f"{name} is missing or empty."
    return True, f"{name} is set."


def validate_anthropic_api_key(
    model: str = "claude-3-haiku-20240307",
    test_prompt: str = "Say hello",
    max_tokens: int = 20,
) -> Tuple[bool, str]:
    """Validate Anthropic API key by performing a lightweight completion."""

    load_dotenv(override=True)
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        return False, "ANTHROPIC_API_KEY is missing."

    client = Anthropic(api_key=key)
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": test_prompt}],
        )
        content_text = (
            resp.content[0].text if getattr(resp, "content", None) else "Validation ok."
        )
        return True, content_text
    except Exception as exc:  # noqa: BLE001
        return False, f"Validation failed: {exc}"


def format_validation_result(provider: str, success: bool, detail: str) -> str:
    """Return a human-friendly validation message."""

    status = "✅" if success else "❌"
    return f"{status} {provider} API key check: {detail}"

