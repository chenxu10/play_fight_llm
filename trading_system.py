class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
    
    def place_order(self, trader_id, side, price, quantity):
        if side == "BUY":
            # Check for matching sell orders
            for i, (ask_price, ask_qty) in enumerate(self.asks):
                if price >= ask_price:
                    # Match found - execute trade
                    if quantity >= ask_qty:
                        # Buy order quantity >= sell order quantity
                        quantity -= ask_qty
                        del self.asks[i]
                        if quantity > 0:
                            self.bids.append((price, quantity))
                        return
                    else:
                        # Partial fill - sell order has remaining quantity
                        self.asks[i] = (ask_price, ask_qty - quantity)
                        return
            # No match found, add to bids
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