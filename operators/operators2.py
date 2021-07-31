def func(n):
    c = str(n)
    add = n
    c_add = c
    for i in range(1,3):
        c_add = c_add + c
        add = add + int(c_add)
    return add

print(func(int(input())))
