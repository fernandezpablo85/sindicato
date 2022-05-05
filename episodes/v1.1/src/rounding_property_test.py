from rounding import percentages
from hypothesis import given, settings, note

from rounding.test_helpers import portfolios


@settings(max_examples=1000)
@given(portfolios())
def test_rounding_should_add_up_to_100(portfolio):
    pcts = percentages(portfolio)
    total = sum(pcts.values())
    assert total == 100
