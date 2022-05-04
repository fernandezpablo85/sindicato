from typing import Dict
from .dumb_rounding import percentages as dumb_percentages


def percentages(portfolio: Dict[str, int]):
    rounded = dumb_percentages(portfolio)
    first_key = list(rounded.keys())[0]
    if sum(rounded.values()) < 100:
        rounded[first_key] += 1
    elif sum(rounded.values()) > 100:
        rounded[first_key] -= 1

    return rounded
