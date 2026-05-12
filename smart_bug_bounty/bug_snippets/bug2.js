function calculateTotal(prices) {
    let total = 0;
    // BUG: Using 'in' instead of 'of' with an array
    for (let price in prices) {
        total += prices[price];
    }
    return total;
}

const items = [10.5, 20, 5];
console.log("Total is: " + calculateTotal(items));


