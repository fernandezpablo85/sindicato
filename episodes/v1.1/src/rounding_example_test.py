from rounding import percentages


def test_rounding_should_add_up_to_100():
    portfolio = {"APPL": 500, "GOOGL": 1_000, "AMZN": 350, "NFLX": 100}
    pcts = percentages(portfolio)
    total = sum(pcts.values())
    assert total == 100
