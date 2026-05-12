cat <<EOF > smart_bug_bounty/bug_snippets/bug1.py
def get_last_n_elements(items, n):
    """Returns the last n elements of a list."""
    if n <= 0:
        return []
    # BUG: Incorrect slicing logic (off-by-one)
    start_index = len(items) - n + 1
    return items[start_index:]

# Example: get_last_n_elements([1, 2, 3], 2) returns [3] instead of [2, 3]
EOF
