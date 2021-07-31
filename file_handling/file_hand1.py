address = "/Users/manas/Desktop/Python_prog/file_handling/test.txt"
t = open(address,'r+')
add_words = t.read()
enter = input("Write whatever you want to enter in the .txt file: ")
add_words = add_words + enter
t.write(add_words)
