import re

def is_valid_email(email):
    """
    Check if a string is a valid email address.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
if __name__ == "__main__":
    print(is_valid_email("user@example.com"))  # Expected: True
    print(is_valid_email("invalid.email"))     # Expected: False