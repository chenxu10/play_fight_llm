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


def test_should_sort_sell_orders_by_price_ascending():
    order_book = OrderBook()
    order_book.place_order("trader_1", "SELL", 50.0, 100)
    order_book.place_order("trader_2", "SELL", 48.0, 50)
    order_book.place_order("trader_3", "SELL", 52.0, 75)
    state = order_book.get_order_book()
    assert state["asks"][0] == (48.0, 50)   # lowest price first
    assert state["asks"][1] == (50.0, 100)
    assert state["asks"][2] == (52.0, 75)   # highest price last


def test_should_match_buy_order_when_bid_price_equals_ask_price():
    order_book = OrderBook()
    order_book.place_order("trader_a", "SELL", 50.0, 100)  # existing sell order
    order_book.place_order("trader_b", "BUY", 50.0, 60)    # matching buy order
    state = order_book.get_order_book()
    # After match, sell order should have remaining quantity
    assert len(state["asks"]) == 1
    assert state["asks"][0] == (50.0, 40)  # 100 - 60 = 40 remaining
    # Buy order should be completely filled (removed from book)
    assert len(state["bids"]) == 0


def test_should_execute_trade_at_makers_price():
    order_book = OrderBook()
    order_book.place_order("trader_a", "SELL", 49.0, 100)  # maker: sell at 49
    trades = order_book.place_order("trader_b", "BUY", 52.0, 60)  # taker: willing to pay 52
    # Trade should execute at maker's price (49.0), not taker's price (52.0)
    assert len(trades) == 1
    price, quantity, buyer_id, seller_id = trades[0]
    assert price == 49.0  # maker's price
    assert quantity == 60
    assert buyer_id == "trader_b"
    assert seller_id == "trader_a"