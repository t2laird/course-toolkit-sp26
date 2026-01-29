# Email Validator (Python)
# Returns True if email format is valid, otherwise False.

import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    print(is_valid_email("example@test.com"))
    print(is_valid_email("bad-email"))
    
    #test
    
