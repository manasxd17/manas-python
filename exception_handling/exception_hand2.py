import re
class InvaidNameError(Exception):
    pass

class InvaidAgeError(Exception):
    pass

class InvaidEmailError(Exception):
    pass

class InvaidPhoneError(Exception):
    pass

class data:
    def __init__(self,mydict):
        self.mydict = mydict
        self.persons = [];
        

    def nameCheck(self):
        if(len(self.mydict['name']) < 2):
            raise InvaidNameError(
                f"Invaid Name entered")
        else:
            self.persons.append(mydict['name'])
        return self.persons

    def ageCheck(self):
        if(self.mydict['age']<0):
            raise InvaidAgeError(
                f"Age should be greater than 0 (Invalid)")
        else:
            self.persons.append(self.mydict['age'])
        return self.persons

    def emailCheck(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.match(regex,self.mydict['email'])):
            self.persons.append(self.mydict['email'])
        else:
            raise InvaidEmailError(
                f"Invaid Email entered")
        return self.persons

    def phoneNumber(self):
        if(len(self.mydict['phone']) != 10):
            raise InvaidPhoneError(
                f"Invaid Phone Number")
        else:
            self.persons.append(self.mydict['phone'])
        return self.persons

mydict = {'name':'Manas','age':21,'email':'manas.maheshwari@gmail','phone':90797571}
d = data(mydict)
print(d.nameCheck())
print(d.ageCheck())
print(d.emailCheck())
print(d.phoneNumber())
        
