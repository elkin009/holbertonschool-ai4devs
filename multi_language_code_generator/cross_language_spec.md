# Cross-Language Specification - Inventory Recommendation Engine

## Algorithm
The algorithm analyzes current stock levels and sales velocity to recommend restock quantities. 
Formula: `Recommendation = (SalesVelocity * LeadTime) - CurrentStock + SafetyStock`
If the result is <= 0, recommendation is 0.

## Input Format
- **Current Stock:** Integer (units on hand)
- **Sales Velocity:** Float (average sales per day)
- **Lead Time:** Integer (days to receive new stock)
- **Safety Stock:** Integer (buffer units)

## Output Format
- **JSON Object:** `{"productId": string, "recommendation": integer, "priority": string}`
- Priority is "High" if stock < safety stock, else "Normal".

## Edge Cases
- **Empty Inventory:** Handle 0 stock gracefully.
- **Negative Sales Velocity:** Treat as 0 sales.
- **Large Inputs:** Ensure no overflow for large stock numbers.
- **Safety Stock > (Sales * LeadTime):** Ensure priority remains "High".

## Test Cases
1. **Normal Case:** Stock=10, Sales=2, Lead=5, Safety=5 -> Output: 5, Priority: "Normal"
2. **Low Stock Case:** Stock=2, Sales=2, Lead=5, Safety=10 -> Output: 18, Priority: "High"
3. **Overstock Case:** Stock=50, Sales=1, Lead=5, Safety=5 -> Output: 0, Priority: "Normal"
4. **Zero Sales Case:** Stock=10, Sales=0, Lead=5, Safety=5 -> Output: 0, Priority: "Normal"
5. **Critical Depletion Case:** Stock=0, Sales=5, Lead=2, Safety=10 -> Output: 20, Priority: "High"
