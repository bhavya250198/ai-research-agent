"""
Quick Anthropic API key validation using shared utilities.
Run: python validate_api_key_anthropic.py
"""

from utilities import (
    format_validation_result,
    validate_anthropic_api_key,
    validate_env_var,
)


def main() -> None:
    """Validate the Anthropic API key and print a friendly status."""

    env_ok, env_detail = validate_env_var("ANTHROPIC_API_KEY")
    if not env_ok:
        print(format_validation_result("Anthropic", False, env_detail))
        return

    success, detail = validate_anthropic_api_key()
    print(format_validation_result("Anthropic", success, detail))


if __name__ == "__main__":
    main()

