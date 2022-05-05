from hypothesis.strategies import composite, lists, floats

assets = ["APPL", "FOO", "BAR", "BAZ", "TSLA", "BTC", "ETH", "SHIB", "DOGE", "SOL"]

total_assets = len(assets)

safe_floats = floats(
    min_value=0.0001,
    max_value=10_000_000,
    allow_infinity=False,
    allow_nan=False,
)


@composite
def portfolios(draw, elements=safe_floats):
    ns = draw(lists(elements, min_size=1, max_size=total_assets))
    return {assets[i % total_assets]: n for i, n in enumerate(ns)}
