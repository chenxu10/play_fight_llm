# Problem 1: Core Trading System Prototype (2 Users)

**Time Allocation: 40 minutes**

## Context
You're building the core of a trading system. For this first iteration, focus on correctness and fundamental design rather than optimization. We need to support exactly 2 traders who can place orders and see their P&L.

## Requirements

### Core Data Structure
Design and implement an **order book** that supports:
- **Buy orders** (bids) - sorted by price descending (highest first)
- **Sell orders** (asks) - sorted by price ascending (lowest first)  
- **Order matching** using price-time priority

### Trading Operations
Implement these core functions:
1. `place_order(trader_id, side, price, quantity)` - where side is "BUY" or "SELL"
2. `get_order_book()` - returns current state of bids and asks
3. `get_trader_pnl(trader_id)` - returns profit/loss for a trader
4. `get_trader_position(trader_id)` - returns current position (quantity held)

### Order Matching Logic
- Orders should match when bid price >= ask price
- Execute at the **maker's price** (existing order in book)
- Partial fills allowed (e.g., buy 100 shares when only 60 available)
- Generate trade executions: `(price, quantity, buyer_id, seller_id)`

## Example Scenario
```
Trader A places: BUY 100 shares at $50
Trader B places: SELL 60 shares at $49
→ Match! Execute 60 shares at $49
→ Trader A still has BUY 40 shares at $50 in book
→ Trader A: position = +60, PnL = -$2940
→ Trader B: position = -60, PnL = +$2940
```

## Deliverables
1. Working code in your preferred language
2. Demonstrate the example scenario above
3. Explain your design choices for the order book data structure

## Evaluation Criteria
- **Correctness** of order matching logic
- **Appropriate data structures** for order book
- **Clear code** that handles edge cases
- **Proper P&L calculation**

## Questions to Consider
- How do you handle partial fills?
- What happens when orders can't be matched?
- How do you track trader positions and P&L over time?

---

*This is a foundation problem. Don't over-engineer - focus on getting the core logic correct. We'll add complexity in subsequent problems.* 