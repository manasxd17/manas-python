import re

def dateCheck(Date):
    if(re.match(r"\D+\s+0[0-9]{1,2}$",Date)):   #Working for month and date only
        return f"Correct Date"
    else:
        return f"Incorrect Date"

print(dateCheck(input()))
