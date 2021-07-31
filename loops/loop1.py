def conCat(mylist:list):
    result = ""
    for words in mylist:
        words = str(words)
        result += words
    return result

print(conCat(["Hi","Bye",17]))
    
