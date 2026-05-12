function calculateSum(numbers) {
    let total = 0;
    if (numbers.length === 0) return 0;
    // BUG: Using 'in'
    for (let index in numbers) {
        total += numbers[index];
    }
    return total;
}

const prices = [10, 20, 30];
console.log(calculateSum(prices));
// Line 13
# Line 14
