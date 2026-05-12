def get_last_elements(items, n):
    if not isinstance(items, list):
        return "Error"
    if n <= 0:
        return []
    # BUG: Off-by-one
    result = items[len(items) - n + 1:]
    return result

data = [1, 2, 3, 4, 5]
print(get_last_elements(data, 3))
# Line 11
# Line 12
# Line 13
