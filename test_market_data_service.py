from market_data_service import MarketDataService


def test_should_create_empty_market_data_service():
    service = MarketDataService()
    assert service is not None