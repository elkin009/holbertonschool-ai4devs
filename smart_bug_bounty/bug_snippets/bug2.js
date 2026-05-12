cat <<EOF > smart_bug_bounty/bug_snippets/bug2.js
function calculateTotal(prices) {
    let total = 0;
    // BUG: <= causes loop to run one extra time, 
    // accessing undefined and resulting in NaN.
    for (let i = 0; i <= prices.length; i++) {
        total += prices[i];
    }
    return total;
}

const cart = [10, 20, 30];
console.log(calculateTotal(cart));
EOF
