from rounding import percentages
from hypothesis import given, settings, note

from rounding.test_helpers import portfolios


def noround(portfolio):
    return {k: v / sum(portfolio.values()) * 100 for k, v in portfolio.items()}


@settings(max_examples=1000)
@given(portfolios())
def test_rounding_should_add_up_to_100(portfolio):
    note(portfolio)
    pcts = percentages(portfolio)
    note(pcts)
    total = sum(pcts.values())
    assert total == 100


@settings(max_examples=1000)
@given(portfolios())
def test_percentages_should_be_all_positive(portfolio):
    note(noround(portfolio))
    pcts = percentages(portfolio)
    note(pcts)
    is_positive = [v > 0 for _, v in pcts.items()]
    assert all(is_positive)
