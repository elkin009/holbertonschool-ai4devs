def get_last_elements(items, n):
    if n <= 0:
        return []
    # BUG: Off-by-one error
    return items[len(items) - n + 1:]

my_list = [10, 20, 30, 40, 50]
print(get_last_elements(my_list, 3))
