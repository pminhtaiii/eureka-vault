
import re

def _norm_option_text(text):
    return " ".join(str(text).strip().casefold().split())

def parse_common_abc(raw_response, options):
    raw = "" if raw_response is None else str(raw_response)
    stripped = raw.strip()

    if stripped in {"A", "B", "C"}:
        return {
            "parsed_choice": stripped,
            "parse_status": "VALID_EXACT",
        }

    m = re.fullmatch(
        r"([ABC])\s*([.):\-])\s*(.+?)",
        stripped,
        flags=re.DOTALL,
    )

    if m:
        choice = m.group(1)
        trailing = m.group(3)

        idx = {"A": 0, "B": 1, "C": 2}[choice]
        if _norm_option_text(trailing) == _norm_option_text(options[idx]):
            return {
                "parsed_choice": choice,
                "parse_status": "VALID_LETTER_OPTION",
            }

    return {
        "parsed_choice": None,
        "parse_status": "INVALID",
    }
