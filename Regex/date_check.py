import re

def dateCheck(Date):
    if re.match(r"(((January|March|May|July|August|October|December)\s(0[1-9]|[12][0-9]|3[01]))|((February)\s(0[1-9]|[12][0-9]|2[0-8]))|((April|June|September|November)\s(0[1-9]|[12][0-9]|3[0])))\s[012](\d){3}", Date):
        return f"Correct Date"
    else:
        return f"Incorrect Date"

print(dateCheck(input("Enter:")))
