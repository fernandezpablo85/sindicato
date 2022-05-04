from rounding import percentages
from hypothesis import given, settings, event
from hypothesis.strategies import floats, lists

assets = ["APPL", "FOO", "BAR", "BAZ", "TSLA", "BTC", "ETH", "SHIB", "DOGE", "SOL"]

total_assets = len(assets)


@settings(max_examples=1000)
@given(
    lists(
        floats(
            min_value=0.0001,
            max_value=10_000_000,
            allow_infinity=False,
            allow_nan=False,
        ),
        min_size=1,
        max_size=total_assets,
    )
)
def test_rounding_should_add_up_to_100(ns):
    portfolio = {assets[i % total_assets]: n for i, n in enumerate(ns)}
    pcts = percentages(portfolio)
    total = sum(pcts.values())
    event(f"total = {total}")
    assert total == 100
