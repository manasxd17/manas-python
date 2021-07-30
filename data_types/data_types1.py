def func(a):
    if(len(a) >= 2):
        return a[:2] + a[-2:]
    else:
        return f"Empty String"

print(func(input()))
