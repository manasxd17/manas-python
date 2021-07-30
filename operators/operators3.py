from datetime import date

def nDays(d1,d2):
    x = d2-d1
    return x.days
    
print(nDays(date(2014,7,2),date(2014,7,11)))
