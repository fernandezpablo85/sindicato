from typing import Dict
from .dumb_rounding import dumb_percentages


def hotfix_percentages(portfolio: Dict[str, int]):
    rounded = dumb_percentages(portfolio)
    first_key = list(rounded.keys())[0]
    delta = 100 - sum(rounded)
    rounded[first_key] += delta
    return rounded
