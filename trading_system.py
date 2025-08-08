class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
    
    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            self.bids.append((price, quantity))
        elif side == "SELL":
            self.asks.append((price, quantity))
    
    def get_order_book(self):
        sorted_bids = sorted(self.bids, key=lambda x: x[0], reverse=True)
        sorted_asks = sorted(self.asks, key=lambda x: x[0])
        return {
            'bids': sorted_bids,
            'asks': sorted_asks
        }