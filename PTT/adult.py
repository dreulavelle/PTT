from pathlib import Path
from typing import Set

def load_adult_keywords(filename: str = "combined-keywords.txt") -> Set[str]:
    """Load adult keywords from the keywords file."""
    keywords_file = Path(__file__).parent / "keywords" / filename
    keywords = set()

    with open(keywords_file, "r") as f:
        for line in f:
            keyword = line.strip().lower()
            if keyword and not keyword.isspace():
                keywords.add(keyword)

    return keywords

# Cached keywords
_adult_keywords: Set[str] | None = None

def get_adult_keywords() -> Set[str]:
    """Get cached adult keywords."""
    global _adult_keywords
    if _adult_keywords is None:
        _adult_keywords = load_adult_keywords()
    return _adult_keywords

def is_adult_content(context):
    if 'adult' in context['result'] and context['result']['adult']:
        return
    """Check if title contains adult content."""
    title_lower = context['title'].lower()
    if any(keyword in title_lower for keyword in get_adult_keywords()):#changed this logic to make tests happy
        context['result']['adult']= True
