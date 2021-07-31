import re

def check_credit(credit):
    if(re.match(r"^[349][\d]{3}(-[\d]{4}){3}$", credit) and not re.search(r"([\d])\1", credit.replace("-", ""))):
        return f"Valid card details"
    else:
        return f"Invalid card details"

print(check_credit(input("Enter:"))) 