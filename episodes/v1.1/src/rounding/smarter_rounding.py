from typing import Dict
from .dumb_rounding import percentages as dumb_percentages


def _hi_key(pcts):
    return max(pcts, key=pcts.get)


def _lo_key(pcts):
    return min(pcts, key=pcts.get)


def percentages(portfolio: Dict[str, int]):
    rounded = dumb_percentages(portfolio)
    delta = 100 - sum(rounded.values())
    key = _lo_key(rounded) if delta > 0 else _hi_key(rounded)
    rounded[key] += delta
    return {k: v for k, v in rounded.items() if v > 0}
