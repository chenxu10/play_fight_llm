# Problem 2: Enterprise Trading System (1,000 Users)

**Time Allocation: 40 minutes**

## Context
Your prototype worked well for 2 users, but now the company wants to deploy this internally for 1,000 employees to trade company stock options and internal instruments. This requires enterprise-grade architecture with proper separation of concerns, data persistence, and scalability considerations.

## System Requirements

### Core Challenge
- Support **1,000 concurrent users** receiving real-time market data
- **Real-time market data** distribution when order book changes

## Architecture Task

Design a system that solves the **real-time data distribution** problem:

### The Problem
Your monolithic order book from Problem 1 works for 2 users, but how do you efficiently broadcast order book updates to 1,000 connected users when trades happen?

### Key Decisions
1. **Message Format**: What data to send on each update  
2. **Scaling Strategy**: How to handle connection management

## Implementation Task

Extend your Problem 1 order book to support **real-time market data distribution**:

```python
# Add this capability to your existing OrderBook class
class MarketDataService:
    def __init__(self):
        self.subscribers = {}  # user_id -> connection
    
    async def subscribe_user(self, user_id, connection):
        # Handle new user subscription
        pass
    
    async def broadcast_order_book_update(self, order_book_state):
        # Send updates to all connected users
        pass
    
    def unsubscribe_user(self, user_id):
        # Clean up when user disconnects
        pass
```

## Key Questions

1. **Message Frequency**: Do you send full order book snapshots or just incremental changes?

2. **Connection Management**: How do you handle 1,000 WebSocket connections efficiently?

3. **Message Ordering**: How do you ensure users receive updates in the correct sequence?

## Deliverables

1. **Working code** that extends your Problem 1 solution
2. **Simple architecture diagram** showing data flow
3. **Demo scenario** with multiple connected users

## Evaluation Criteria

- **Protocol choice** and justification (70%)
- **Code implementation** quality (20%)
- **Scalability considerations** (10%)

---

*This problem tests your ability to design production-ready systems. Focus on architectural decisions that will matter at enterprise scale.