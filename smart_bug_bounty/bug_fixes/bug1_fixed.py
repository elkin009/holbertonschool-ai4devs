def calculate_discount(price, discount_percent):
    if not isinstance(price, (int, float)):
        raise TypeError('Price must be a number')
    if not isinstance(discount_percent, (int, float)):
        raise TypeError('Discount must be a number')
    if discount_percent < 0:
        return 'Invalid discount'
    if discount_percent > 100:
        return 'Invalid discount'
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

def get_top_students(students, n):
    if not students:
        return []
    if n <= 0:
        return []
    sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
    return sorted_students[:n]

if __name__ == "__main__":
    prices = [100, 200, 300]
    for p in prices:
        result = calculate_discount(p, 20)
        assert result == p * 0.8, f"Test failed for price {p}"
    print("Test 1 passed - calculate_discount works correctly")

    students = [
        {'name': 'Alice', 'score': 92},
        {'name': 'Bob', 'score': 78},
        {'name': 'Carol', 'score': 88}
    ]
    top = get_top_students(students, 2)
    assert top[0]['name'] == 'Alice', f"Test failed: {top}"
    assert top[1]['name'] == 'Carol', f"Test failed: {top}"
    print("Test 2 passed - get_top_students returns correct top students")

    assert get_top_students([], 2) == []
    print("Test 3 passed - empty list returns empty")
    print("All tests passed for bug1_fixed.py")
