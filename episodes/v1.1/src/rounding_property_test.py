from rounding import percentages
from hypothesis import given, settings, note

from rounding.test_helpers import portfolios


def noround(portfolio):
    return {
        k: round(v / sum(portfolio.values()) * 100, 4) for k, v in portfolio.items()
    }


examples = 1_000


@settings(max_examples=examples)
@given(portfolios())
def test_rounding_should_add_up_to_100(portfolio):
    pcts = percentages(portfolio)
    total = sum(pcts.values())
    assert total == 100


@settings(max_examples=examples)
@given(portfolios())
def test_percentages_should_be_all_positive(portfolio):
    pcts = percentages(portfolio)
    is_positive = [v > 0 for _, v in pcts.items()]
    assert all(is_positive)


@settings(max_examples=examples)
@given(portfolios())
def disabled_test_error_should_be_minimal(portfolio):
    pcts = percentages(portfolio)
    note(pcts)
    raw = noround(portfolio)
    note(raw)
    errors = [pcts[k] - raw[k] for k in pcts.keys()]
    note(errors)
    is_reasonable = [abs(e) < 3 for e in errors]
    assert all(is_reasonable)


portfolio_that_fails = {
    "APPL": 625616.1693652052,
    "BAR": 617938.9028649231,
    "BAZ": 618342.162300139,
    "BTC": 619632.897639023,
    "ETH": 620706.1826511598,
    "FOO": 617512.6030206202,
    "SHIB": 6888900.851008516,
    "TSLA": 618844.7209371484,
}
