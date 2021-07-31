def Error():
    try:
        mylist = ["Hi","Bye","K"]   
        print(mylist[4])     #IndexError

        print(int("Hello World"))   #ValueError

        a = 50
        print(a/0)   #ZeroDivisionError

        len(50)      #TypeError

        my_dict = {'Name':'Manas','Age':21}
        print(my_dict['course'])      #KeyError

    except IndexError:
        print("Index Error")

    except ValueError:
        print("Value Error")

    except ZeroDivisionError:
        print("Zero division error")

    except TypeError:
        print("Type Error")

    except KeyError:
        print("Key Error")

Error()
        

    
