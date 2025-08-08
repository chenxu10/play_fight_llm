import pytest
from trading_system import OrderBook


def test_should_create_empty_order_book():
    order_book = OrderBook()
    assert order_book is not None