import pytest
from trading_system import OrderBook


def test_should_create_empty_order_book():
    order_book = OrderBook()
    assert order_book is not None


def test_should_place_single_buy_order():
    order_book = OrderBook()
    order_book.place_order("trader_a", "BUY", 50.0, 100)
    # Test passes if no exception is raised