cat <<EOF > smart_bug_bounty/bug_snippets/bug4.py
def add_to_registry(name, registry=[]):
    """Adds a name to a provided or default registry list."""
    # BUG: The default list persists across multiple function calls.
    registry.append(name)
    return registry

print(add_to_registry("Alice")) # ['Alice']
print(add_to_registry("Bob"))   # Expected ['Bob'], Actual ['Alice', 'Bob']
EOF
