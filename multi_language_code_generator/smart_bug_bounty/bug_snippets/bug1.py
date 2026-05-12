def get_last_n(items, n):
    return items[len(items)-n+1:] # Off-by-one error
