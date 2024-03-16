import re

STRING_LOGIC_START = "Running {step} logic"
STRING_LOGIC_END = "{step} logic successfully completed"


def clean_text(text: str) -> str:
    """
    Clean text by removing extra spaces and replacing hyphens and underscores with spaces.

    Args:
        text (str): Text to clean.

    Returns:
        str: Cleaned text.
    """
    cleaned_text = re.sub(r"[_-]", " ", text)
    return " ".join(cleaned_text.strip().split()).title()
