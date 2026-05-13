def get_last_n_items(items, n):
    if n <= 0:
        return []
    if n >= len(items):
        return items
    return items[len(items) - n:]

if __name__ == '__main__':
    assert get_last_n_items([1,2,3,4,5], 3) == [3,4,5]
    print('Test 1 passed')
    assert get_last_n_items([1,2,3,4,5], 1) == [5]
    print('Test 2 passed')
    assert get_last_n_items([1,2,3,4,5], 5) == [1,2,3,4,5]
    print('Test 3 passed')
    print('All tests passed for bug1_fixed.py')
