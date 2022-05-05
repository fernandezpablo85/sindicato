from typing import Dict
from .dumb_rounding import percentages as dumb_percentages


def percentages(portfolio: Dict[str, int]):
    rounded = dumb_percentages(portfolio)
    first_key = list(rounded.keys())[0]
    delta = 100 - sum(rounded.values())
    rounded[first_key] += delta
    return rounded
