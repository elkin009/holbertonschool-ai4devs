def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"

def parse_config(config_str):
    config = {}
    lines = config_str.split('\n')
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()
    return config

def connect_database(host, port, password):
    connection_string = f"host={host};port={port};password={password}"
    print(f"Connecting to: host={host};port={port}")
    return connection_string

def validate_user(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return query, (username, password)

if __name__ == "__main__":
    result = read_file('nonexistent.txt')
    assert 'Error' in result, f"Test 1 failed: {result}"
    print("Test 1 passed - missing file handled gracefully")

    config = parse_config('host=localhost\nport=5432\nbroken_line')
    assert config['host'] == 'localhost', f"Test 2 failed: {config}"
    assert config['port'] == '5432', f"Test 2 failed: {config}"
    print("Test 2 passed - parse_config handles broken lines")

    cs = connect_database('localhost', 5432, 'mypassword')
    assert 'mypassword' in cs, f"Test 3 failed: {cs}"
    assert 'admin123' not in cs, f"Test 3 failed - hardcoded password still present"
    print("Test 3 passed - connect_database uses supplied password")

    query, params = validate_user('alice', 'pass123')
    assert '?' in query, f"Test 4 failed: {query}"
    assert params == ('alice', 'pass123'), f"Test 4 failed: {params}"
    print("Test 4 passed - validate_user uses parameterized query")
    print("All tests passed for bug5_fixed.py")
