import re
from typing import Dict, Any, Optional, Callable

# Importing Transformer functions from transformers.py
from .transformers import none, value, integer, boolean, lowercase, uppercase, date, range_transform, year_range, array, uniq_concat

class Parser:
    def __init__(self):
        self.handlers = []

    def add_handler(self, name: str, reg_exp: re.Pattern, transformer: Optional[Callable] = None, options: Optional[Dict[str, Any]] = None):
        options = options or {}
        transformer = transformer if transformer is not None else none
        self.handlers.append({"name": name, "reg_exp": reg_exp, "transformer": transformer, "options": options})

    def _create_handler_from_regex(self, name: str, reg_exp: re.Pattern, transformer: Callable, options: Dict[str, Any]) -> Callable:
        def handler(title: str, result: Dict[str, Any], matched: Dict[str, Any]) -> None:
            if result.get(name) and options.get("skip_if_already_found", False):
                return

            match = reg_exp.search(title)
            if match:
                raw_match, clean_match = match.group(), match.group(1) if match.groups() else match.group()
                transformed = transformer(clean_match)
                result[name] = transformed
                if options.get("remove", False):
                    result["title"] = title.replace(raw_match, "")

        return handler

    def parse(self, title: str) -> Dict[str, Any]:
        result = {}
        matched = {}
        for handler in self.handlers:
            handler_func = self._create_handler_from_regex(**handler)
            handler_func(title, result, matched)

        result["title"] = self._clean_title(title)
        return result

    @staticmethod
    def _clean_title(raw_title: str) -> str:
        cleaned_title = re.sub(r"[_]+", " ", raw_title)
        cleaned_title = re.sub(r"^\[([^[\]]+)]", "", cleaned_title)
        cleaned_title = re.sub(r"(.+)\[([^[\]]+)]$", r"\1", cleaned_title)
        return cleaned_title.strip()

    def add_defaults(self):
        # Episode Code
        self.add_handler("episodeCode", re.compile(r"\[([A-Z0-9]{8})\]"), uppercase, {"remove": True})

        # Resolution
        self.add_handler("resolution", re.compile(r"\b4k\b", re.IGNORECASE), value("4K"), {"remove": True})
        self.add_handler("resolution", re.compile(r"2160[pi]", re.IGNORECASE), value("4K"), {"remove": True, "skip_if_already_found": False})

        # Date
        self.add_handler("date", re.compile(r"(19[6-9]|20[01])\d-[01]\d-[0-3]\d"), date("YYYY-MM-DD"), {"remove": True})

        # Year
        self.add_handler("year", re.compile(r"\b(19\d{2}|20[01]\d)\b"), integer, {"remove": True})

        # Extended
        self.add_handler("extended", re.compile(r"EXTENDED", re.IGNORECASE), boolean, {"remove": True})

        # Convert
        self.add_handler("convert", re.compile(r"CONVERT", re.IGNORECASE), boolean, {"remove": True})

        # Hardcoded
        self.add_handler("hardcoded", re.compile(r"HC|HARDCODED", re.IGNORECASE), boolean, {"remove": True})

        # Proper
        self.add_handler("proper", re.compile(r"PROPER", re.IGNORECASE), boolean, {"remove": True})

        # Repack
        self.add_handler("repack", re.compile(r"REPACK|RERIP", re.IGNORECASE), boolean, {"remove": True})

        # Retail
        self.add_handler("retail", re.compile(r"\bRetail\b", re.IGNORECASE), boolean, {"remove": True})

        # Remastered
        self.add_handler("remastered", re.compile(r"\bRemastered\b", re.IGNORECASE), boolean, {"remove": True})

        # Unrated
        self.add_handler("unrated", re.compile(r"\bUnrated|Uncensored\b", re.IGNORECASE), boolean, {"remove": True})

        # Region
        self.add_handler("region", re.compile(r"R\d"), none, {"skip_if_first": True})

        # Source
        self.add_handler("source", re.compile(r"\bCAM\b", re.IGNORECASE), value("CAM"), {"remove": True})