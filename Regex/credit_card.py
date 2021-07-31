import re

def check(credit):
    if (re.match(r'^[349]\d{3}-\d{4}\-\d{4}\-\d{4}$',credit)):
        return f"Valid Card number"
    else:
        return f"Invalid Card number"

print(check(input()))