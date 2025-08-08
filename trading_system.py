import heapq
from typing import List, Tuple, Dict

class OrderBook:
    def __init__(self):
        self.bids = []  # max-heap: store as (-price, quantity, trader_id)
        self.asks = []  # min-heap: store as (price, quantity, trader_id)
        self.positions = {}  # trader_id -> position (positive = long, negative = short)
        self.pnl = {}  # trader_id -> profit/loss from trades
    
    def _try_match_buy_order(self, buyer_id, price, quantity):
        """
        Match buy order against existing sell orders (asks heap)
        Asks are min-heap, so we can efficiently get lowest price
        """
        trades = []
        while self.asks and quantity > 0 and price >= self.asks[0][0]:
            ask_price, ask_qty, seller_id = heapq.heappop(self.asks)
            
            if quantity >= ask_qty:
                # Complete fill of sell order
                trades.append((ask_price, ask_qty, buyer_id, seller_id))
                # Update positions and PnL
                self.positions[buyer_id] = self.positions.get(buyer_id, 0) + ask_qty
                self.positions[seller_id] = self.positions.get(seller_id, 0) - ask_qty
                self.pnl[buyer_id] = self.pnl.get(buyer_id, 0) - (ask_price * ask_qty)
                self.pnl[seller_id] = self.pnl.get(seller_id, 0) + (ask_price * ask_qty)
                quantity -= ask_qty
            else:
                # Partial fill of sell order - put remainder back
                trades.append((ask_price, quantity, buyer_id, seller_id))
                # Update positions and PnL
                self.positions[buyer_id] = self.positions.get(buyer_id, 0) + quantity
                self.positions[seller_id] = self.positions.get(seller_id, 0) - quantity
                self.pnl[buyer_id] = self.pnl.get(buyer_id, 0) - (ask_price * quantity)
                self.pnl[seller_id] = self.pnl.get(seller_id, 0) + (ask_price * quantity)
                heapq.heappush(self.asks, (ask_price, ask_qty - quantity, seller_id))
                quantity = 0
        
        return quantity, trades

    def _try_match_sell_order(self, seller_id, price, quantity):
        """
        Match sell order against existing buy orders (bids max-heap)
        Bids are max-heap (stored as negative), so we can efficiently get highest price
        """
        trades = []
        while self.bids and quantity > 0 and price <= -self.bids[0][0]:
            neg_bid_price, bid_qty, buyer_id = heapq.heappop(self.bids)
            bid_price = -neg_bid_price  # Convert back from negative
            
            if quantity >= bid_qty:
                # Complete fill of buy order
                trades.append((bid_price, bid_qty, buyer_id, seller_id))
                # Update positions and PnL
                self.positions[buyer_id] = self.positions.get(buyer_id, 0) + bid_qty
                self.positions[seller_id] = self.positions.get(seller_id, 0) - bid_qty
                self.pnl[buyer_id] = self.pnl.get(buyer_id, 0) - (bid_price * bid_qty)
                self.pnl[seller_id] = self.pnl.get(seller_id, 0) + (bid_price * bid_qty)
                quantity -= bid_qty
            else:
                # Partial fill of buy order - put remainder back
                trades.append((bid_price, quantity, buyer_id, seller_id))
                # Update positions and PnL
                self.positions[buyer_id] = self.positions.get(buyer_id, 0) + quantity
                self.positions[seller_id] = self.positions.get(seller_id, 0) - quantity
                self.pnl[buyer_id] = self.pnl.get(buyer_id, 0) - (bid_price * quantity)
                self.pnl[seller_id] = self.pnl.get(seller_id, 0) + (bid_price * quantity)
                heapq.heappush(self.bids, (-bid_price, bid_qty - quantity, buyer_id))
                quantity = 0
        
        return quantity, trades

    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            remaining_quantity, trades = self._try_match_buy_order(trader_id, price, quantity)
            if remaining_quantity > 0:
                heapq.heappush(self.bids, (-price, remaining_quantity, trader_id))  # negative for max-heap
            return trades
        elif side == "SELL":
            remaining_quantity, trades = self._try_match_sell_order(trader_id, price, quantity)
            if remaining_quantity > 0:
                heapq.heappush(self.asks, (price, remaining_quantity, trader_id))  # positive for min-heap
            return trades
    
    def get_order_book(self):
        # Heaps are already ordered! Just need to convert format
        # For bids: convert negative prices back to positive and sort by negative (max-heap order)
        # For asks: already in min-heap order
        sorted_bids = sorted(self.bids, key=lambda x: x[0])  # sort by negative price (highest first)
        sorted_asks = sorted(self.asks, key=lambda x: x[0])  # sort by positive price (lowest first)
        
        # Return just price and quantity for backward compatibility
        bids_simple = [(-neg_price, qty) for neg_price, qty, trader_id in sorted_bids]
        asks_simple = [(price, qty) for price, qty, trader_id in sorted_asks]
        return {
            'bids': bids_simple,
            'asks': asks_simple
        }
    
    def get_trader_position(self, trader_id):
        return self.positions.get(trader_id, 0)
    
    def get_trader_pnl(self, trader_id):
        return self.pnl.get(trader_id, 0.0)