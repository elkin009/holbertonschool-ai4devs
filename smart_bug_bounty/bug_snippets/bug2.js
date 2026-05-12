/**
 * Calculates the total sum of prices in a shopping cart array.
 * Includes a check for empty arrays.
 */
function calculateCartTotal(prices) {
    let total = 0;
    if (prices.length === 0) {
        return 0;
    }

    // BUG: Using 'for...in' on an array retrieves keys (strings) 
    // instead of values, causing unexpected results.
    for (let price in prices) {
        total += prices[price];
    }
    
    return total;
}

const userCart = [15.99, 23.50, 4.00, 10.00];
console.log("Processing cart sum...");
console.log("The final calculated total is: " + calculateCartTotal(userCart));
