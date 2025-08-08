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
    order_book.place_order("trader_a","BUY", 50, 100)
    state = order_book.get_order_book()
    assert state["bids"][0] == (50,100)

def test_should_return_order_book_state_with_single_sell_order():
    order_book = OrderBook()
    order_book.place_order("trader_b", "SELL", 49.0, 60)
    state = order_book.get_order_book()
    assert "asks" in state
    assert len(state["asks"]) == 1
    assert state["asks"][0] == (49.0, 60)

def test_should_sort_buy_orders_by_price_descending():
    order_book = OrderBook()
    order_book.place_order("trader_1", "BUY", 50.0, 100)
    order_book.place_order("trader_2", "BUY", 52.0, 50)
    order_book.place_order("trader_3", "BUY", 48.0, 75)
    state = order_book.get_order_book()
    assert state["bids"][0] == (52.0, 50)  # highest price first
    assert state["bids"][1] == (50.0, 100)
    assert state["bids"][2] == (48.0, 75)   # lowest price last