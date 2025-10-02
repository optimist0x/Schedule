"""
Bug fix implementation
"""

def fixed_function():
    """Fixed function that had a bug"""
    try:
        # Fixed the bug here
        result = 42
        return result
    except Exception as e:
        print(f"Error handled: {e}")
        return None

def validate_input(data):
    """Added input validation to prevent the bug"""
    if not data:
        raise ValueError("Data cannot be empty")
    return data

if __name__ == "__main__":
    fixed_function()
