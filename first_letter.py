
def input_check():
    try :
        input1 = int(input("Enter a number : "))
        return input1
    except ValueError:
        print("That was not an integer")



for i in range(3):
    test = input_check()
    if(str("<class 'int'>") == str(type(test))):
        break
    else:
        print("try again ")

else:
    print("Input is invalid")
        

    