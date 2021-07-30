class check:

    def __init__(self):
        pass

    def checkIs(self,string):
        if (string.startswith("Is")):
            return string
        else:
            return f"Is {string}"


    def Evenodd(self,a):
        if(a % 2 == 0):
            return f"Even"
        else:
            return f"Odd"


    def vowel(self,l):
        if(l in ('a','e','i','o','u')):
            return f"Vowel"
        else:
            return f"Consonant"


c = check()
print(c.checkIs(str(input())))
print(c.Evenodd(int(input())))
print(c.vowel(input()))
