from pathlib import Path
from typing import Set

import regex


def load_adult_keywords(filename: str = "combined-keywords.txt") -> Set[str]:
    """Load adult keywords from the keywords file."""
    keywords_file = Path(__file__).parent / "keywords" / filename
    keywords = set()

    with open(keywords_file, "r") as f:
        for line in f:
            keyword = line.strip()
            if keyword and not keyword.isspace():
                keywords.add(regex.escape(keyword))

    return keywords


def create_adult_pattern() -> regex.Pattern:
    """Create a compiled regex pattern for adult content detection."""
    keywords = load_adult_keywords()
    return regex.compile(r"\b(" + "|".join(keywords) + r")\b", regex.IGNORECASE)
