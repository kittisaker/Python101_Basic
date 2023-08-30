def doubles(number):
    return number * 2


number = input("Please enter a number : ")

try:
    num = int(number)
    for i in range(3):
        num = doubles(num)
        print(num)
except ValueError:
    print("Invalid input, Please enter a number")