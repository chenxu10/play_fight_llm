# Trading System TDD Plan

## Test Implementation Plan (Red → Green → Refactor)

Each test should be implemented one at a time, following strict TDD methodology.

### Phase 1: Basic Order Book Structure
- [ ] Test 1: Should create empty order book
- [ ] Test 2: Should place a single buy order
- [ ] Test 3: Should place a single sell order
- [ ] Test 4: Should return order book state with single buy order
- [ ] Test 5: Should return order book state with single sell order

### Phase 2: Order Book Sorting
- [ ] Test 6: Should sort buy orders by price descending (highest first)
- [ ] Test 7: Should sort sell orders by price ascending (lowest first)
- [ ] Test 8: Should maintain price-time priority for same-price orders

### Phase 3: Basic Matching Logic
- [ ] Test 9: Should match buy order when bid price equals ask price
- [ ] Test 10: Should match buy order when bid price exceeds ask price
- [ ] Test 11: Should not match when bid price is below ask price
- [ ] Test 12: Should execute trade at maker's price (existing order price)

### Phase 4: Position and PnL Tracking
- [ ] Test 13: Should track trader position after buy execution
- [ ] Test 14: Should track trader position after sell execution
- [ ] Test 15: Should calculate basic PnL for buyer
- [ ] Test 16: Should calculate basic PnL for seller

### Phase 5: Partial Fills
- [ ] Test 17: Should handle partial fill when buy quantity exceeds sell quantity
- [ ] Test 18: Should handle partial fill when sell quantity exceeds buy quantity
- [ ] Test 19: Should leave remaining quantity in order book after partial fill

### Phase 6: Multiple Orders and Complex Scenarios
- [ ] Test 20: Should handle multiple orders at different price levels
- [ ] Test 21: Should implement the example scenario from requirements
- [ ] Test 22: Should handle edge cases (zero quantities, invalid trader IDs)

## Implementation Notes
- Use Python with pytest for testing
- Follow Kent Beck's TDD cycle strictly: Red → Green → Refactor
- Make structural changes (Tidy First) separate from behavioral changes
- Commit frequently with clear commit messages
- Each test should focus on one small behavior increment