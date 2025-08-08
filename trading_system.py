class OrderBook:
    def __init__(self):
        self.bids = []
    
    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            self.bids.append((price, quantity))
    
    def get_order_book(self):
        return {"bids": self.bids}