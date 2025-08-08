# Trading System TDD Plan

## Test Implementation Plan (Red → Green → Refactor)

Each test should be implemented one at a time, following strict TDD methodology.

### Phase 1: Basic Order Book Structure
- [x] Test 1: Should create empty order book
- [x] Test 2: Should place a single buy order
- [x] Test 3: Should place a single sell order
- [x] Test 4: Should return order book state with single buy order
- [x] Test 5: Should return order book state with single sell order

### Phase 2: Order Book Sorting
- [x] Test 6: Should sort buy orders by price descending (highest first)
- [x] Test 7: Should sort sell orders by price ascending (lowest first)
- [ ] Test 8: Should maintain price-time priority for same-price orders

### Phase 3: Basic Matching Logic
- [x] Test 9: Should match buy order when bid price equals ask price
- [ ] Test 10: Should match buy order when bid price exceeds ask price
- [ ] Test 11: Should not match when bid price is below ask price
- [x] Test 12: Should execute trade at maker's price (existing order price)

### Phase 4: Position and PnL Tracking
- [x] Test 13: Should track trader position after buy execution
- [ ] Test 14: Should track trader position after sell execution
- [ ] Test 15: Should calculate basic PnL for buyer
- [x] Test 16: Should calculate basic PnL for seller


## Implementation Notes
- Use Python with pytest for testing
- Follow Kent Beck's TDD cycle strictly: Red → Green → Refactor
- Make structural changes (Tidy First) separate from behavioral changes
- Commit frequently with clear commit messages
- Each test should focus on one small behavior increment