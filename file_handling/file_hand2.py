address = "/Users/manas/Desktop/Python_prog/file_handling/test1.csv"
try:    
    s = open(address, 'r+')
    words = s.readlines()
    header = words[0].strip('\n').split('  ')
    print(f'{header[0]}  {header[1]}')
    for i in range(1, len(words)):
        letters = words[i].strip('\n').split('  ')
        print(f'{letters[0]},{letters[1]}')
        new = "\n3  Superman"
        s.write(new)

    print("Open the new file")
    print(f'{header[0]}  {header[1]}')
    s = open(address, 'r')
    words = s.readlines()
    for i in range(1, len(words)):
        letters = words[i].strip('\n').split('  ')
        print(f'{letters[0]}  {letters[1]}')


except Exception as e:
    print(e)