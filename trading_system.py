class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
    
    def _try_match_buy_order(self, price, quantity):
        """
        This function tries to find the remaining quantitiy after matching
        with bids
        """
        for i, (ask_price, ask_qty) in enumerate(self.asks):
            if price >= ask_price:
                if quantity >= ask_qty:
                    quantity -= ask_qty
                    del self.asks[i]
                    return quantity
                else:
                    self.asks[i] = (ask_price, ask_qty - quantity)
                    return 0
        return quantity

    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            remaining_quantity = self._try_match_buy_order(price, quantity)
            if remaining_quantity > 0:
                self.bids.append((price, remaining_quantity))
        elif side == "SELL":
            self.asks.append((price, quantity))
    
    def get_order_book(self):
        sorted_bids = sorted(self.bids, key=lambda x: x[0], reverse=True)
        sorted_asks = sorted(self.asks, key=lambda x: x[0])
        return {
            'bids': sorted_bids,
            'asks': sorted_asks
        }