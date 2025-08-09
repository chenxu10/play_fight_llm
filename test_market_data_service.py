from market_data_service import MarketDataService


def test_should_create_empty_market_data_service():
    service = MarketDataService()
    assert service is not None


def test_should_initialize_with_empty_subscribers_dictionary():
    service = MarketDataService()
    assert hasattr(service, 'subscribers')
    assert service.subscribers == {}


def test_should_have_subscribe_user_method():
    service = MarketDataService()
    assert hasattr(service, 'subscribe_user')
    assert callable(service.subscribe_user)