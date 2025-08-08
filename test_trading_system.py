import pytest
from trading_system import OrderBook


def test_should_create_empty_order_book():
    order_book = OrderBook()
    assert order_book is not None


def test_should_place_single_buy_order():
    order_book = OrderBook()
    order_book.place_order("trader_a", "BUY", 50.0, 100)
    # Test passes if no exception is raised


def test_should_place_single_sell_order():
    order_book = OrderBook()
    order_book.place_order("trader_b", "SELL", 49.0, 60)
    # Test passes if no exception is raised


def test_should_return_order_book_state_with_single_buy_order():
    order_book = OrderBook()
    order_book.place_order("trader_a", "BUY", 50.0, 100)
    state = order_book.get_order_book()
    assert "bids" in state
    assert len(state["bids"]) == 1
    assert state["bids"][0] == (50.0, 100)