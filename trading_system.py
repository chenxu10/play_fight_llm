class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
        self.positions = {}  # trader_id -> position (positive = long, negative = short)
    
    def _try_match_buy_order(self, buyer_id, price, quantity):
        """
        This function tries to find the remaining quantitiy after matching
        with bids
        """
        trades = []
        for i, (ask_price, ask_qty, seller_id) in enumerate(self.asks):
            if price >= ask_price:
                if quantity >= ask_qty:
                    # Complete fill of sell order
                    trades.append((ask_price, ask_qty, buyer_id, seller_id))
                    # Update positions
                    self.positions[buyer_id] = self.positions.get(buyer_id, 0) + ask_qty
                    self.positions[seller_id] = self.positions.get(seller_id, 0) - ask_qty
                    quantity -= ask_qty
                    del self.asks[i]
                    if quantity == 0:
                        break
                else:
                    # Partial fill of sell order
                    trades.append((ask_price, quantity, buyer_id, seller_id))
                    # Update positions
                    self.positions[buyer_id] = self.positions.get(buyer_id, 0) + quantity
                    self.positions[seller_id] = self.positions.get(seller_id, 0) - quantity
                    self.asks[i] = (ask_price, ask_qty - quantity, seller_id)
                    quantity = 0
                    break
        return quantity, trades

    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            remaining_quantity, trades = self._try_match_buy_order(trader_id, price, quantity)
            if remaining_quantity > 0:
                self.bids.append((price, remaining_quantity, trader_id))
            return trades
        elif side == "SELL":
            self.asks.append((price, quantity, trader_id))
            return []
    
    def get_order_book(self):
        sorted_bids = sorted(self.bids, key=lambda x: x[0], reverse=True)
        sorted_asks = sorted(self.asks, key=lambda x: x[0])
        # Return just price and quantity for backward compatibility
        bids_simple = [(price, qty) for price, qty, trader_id in sorted_bids]
        asks_simple = [(price, qty) for price, qty, trader_id in sorted_asks]
        return {
            'bids': bids_simple,
            'asks': asks_simple
        }
    
    def get_trader_position(self, trader_id):
        return self.positions.get(trader_id, 0)