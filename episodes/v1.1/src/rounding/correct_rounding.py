from typing import Dict
from math import floor
from itertools import zip_longest


def _decimal_part(n):
    return n - floor(n)


def percentages(portfolio: Dict[str, int]):
    total = sum(portfolio.values())
    noround = {k: v / total * 100 for k, v in portfolio.items()}
    sorted_by_decimal_part = sorted(
        noround.items(), key=lambda t: _decimal_part(t[1]), reverse=True
    )
    floored = [(k, floor(v)) for k, v in sorted_by_decimal_part]
    diff = 100 - sum(v for _, v in floored)
    deltas = [1] * diff
    rounded = {k: a + b for (k, a), b in zip_longest(floored, deltas, fillvalue=0)}
    return {k: v for k, v in rounded.items() if v > 0}
