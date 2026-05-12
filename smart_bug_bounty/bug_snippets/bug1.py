def get_last_elements(items, n):
    """
    This function is designed to return the last n elements from a list.
    It includes basic validation for the input parameters.
    """
    if not isinstance(items, list):
        return "Input must be a list"
    if n <= 0:
        return []
    
    # BUG: Off-by-one error in the slice logic
    # It should be items[-n:]
    result = items[len(items) - n + 1:]
    return result

# Test the function with sample data
data_list = [10, 20, 30, 40, 50]
n_to_return = 3
print(f"Requesting last {n_to_return} items from {data_list}")
print("Result:", get_last_elements(data_list, n_to_return))
