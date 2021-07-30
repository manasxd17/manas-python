def maxFunc(mylist:list):
    max = mylist[0]
    for i in mylist:
        if i > max:
            max=i
    return max

print(maxFunc(input().split()))
