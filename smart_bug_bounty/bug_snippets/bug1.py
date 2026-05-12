def get_last_elements(items, n):
    if not isinstance(items, list):
        return "Error"
    if n <= 0:
        return []
    # BUG
    return items[len(items) - n + 1:]

data = [1, 2, 3, 4, 5]
print(get_last_elements(data, 3))
# Line 10
# Line 11
