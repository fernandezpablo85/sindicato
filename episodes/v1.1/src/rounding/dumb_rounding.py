from typing import Dict


def percentages(portfolio: Dict[str, int]):
    total = sum(portfolio.values())
    return {k: round((v / total) * 100) for k, v in portfolio.items()}
