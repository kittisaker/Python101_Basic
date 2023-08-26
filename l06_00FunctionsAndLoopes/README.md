# Function and Loopes

## 1. What is a Function?
### Functions Are Values
```
>>> len
<built-in function len>
>>> type(len)
<class 'builtin_function_or_method'>
>>> len = "i'm not the len you're looking for."
>>> len
"i'm not the len you're looking for."
>>> type(len)
<class 'str'>

>>> del len
>>> len
<built-in function len>
```

### How Python Executes Functions
```
>>> num_letters = len("four")
>>> num_letters
4
```

### Functions Can Have Side Effects
```
>>> return_value = print("What do I return?")
What do I return?
>>> return_value
>>>

>>> type(return_value)
<class 'NoneType'>
>>> print(return_value)
None
```

## 2. Write Your Own Functions

### The Anatomy of a Function
```
def multiply(x, y):     #Function signature
    # Function body
    product = x * y
    return product
```

### The Function Signature
```
def multiply(x, y):

1. The def keyword
2. The function name, multiply
3. The parameter list, (x, y)
4. A colon (:) at the end of the line
```

### The Function Body
```
def multiply(x, y):     #Function signature
    # Function body
    product = x * y
    return product
    print("You can't see me!")
```

### Calling a User-Defined Function
```
print(multiply(2, 4))

def multiply(x, y):
    return x * y

> python .\first_letter.py
Traceback (most recent call last):
  File "D:\Projects_Python\Ebook\Python101Basics\first_letter.py", line 1, in <module>
    print(multiply(2, 4))
          ^^^^^^^^
NameError: name 'multiply' is not defined
```

```
def multiply(x, y):
    return x * y

print(multiply(2, 4))

> python .\first_letter.py
8
```

### Functions With No Return Statement
```
def greet(name):
    print(f"Hello, {name} !")

greet("Solo Dev")                   # Hello, Solo Dev !

return_value = greet("Solo Dev")    # Hello, Solo Dev !

print(return_value)                 # None
```

### Documenting Your Functions
```
>>> help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

```
def multiply(x, y):
    """Return the product of two number x and y."""
    product = x * y
    return product

help(multiply)

> python .\first_letter.py
Help on function multiply in module __main__:

multiply(x, y)
    Return the product of two number x and y.
```

## 3. Challenge : Convert Temperatures
```
Write a script called temperature.py that defines two functions:

1. convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:

F = C * 9/5 + 32


2. convert_far_to_cel() which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:

C = (F - 32) * 5/9
```

```
def convert_cel_to_far(C):
    F = float(C) * 9/5 + 32
    return F

def convert_far_to_cel(F):
    C = (float(F) - 32) * 5/9
    return C

F = input("Enter a temperature in degrees F : ")
print("{} degree F = {:.2f} C" .format(F, convert_far_to_cel(F)))

C = input("Enter a temperature in degree C : ")
print("{} degrees C = {:.2f} F" .format(C, convert_cel_to_far(C)))
```

## 4. Report a Block of Code

### The while Loop
```
num = float(input("Enter a positive number : "))

while num <= 0:
    print("That's not a posiive numbe!")
    num = float(input("Enter a positive number : "))
    print("Good bye")

print("I'm not in loop while")
```

### The for Loop
```
for letter in "Python":
    print(letter)

# > python .\first_letter.py
# P
# y
# t
# h
# o
# n
```

```
index = 0
word = "Python"

while index < len(word):
    print(word[index])
    index = index + 1

# P
# y
# t
# h
# o
# n
```

```
for n in range(3):
    print("Python")

# Python
# Python
# Python
```

```
for n in range(10, 20):
    print(n * n)

# 100
# 121
# 144
# 169
# 196
# 225
# 256
# 289
# 324
# 361
```

```
amount = float(input("Enter an amoutn : "))

for num_people in range(2, 6):
    print(f"{num_people} people : $ {amount / num_people:.2f} each")

# Enter an amoutn : 4
# 2 people : $ 2.00 each
# 3 people : $ 1.33 each
# 4 people : $ 1.00 each
# 5 people : $ 0.80 each
```

### Nested Loops
```
for n in range(1, 3):
    for j in range(4, 6):
        print(f"n = {n} and j = {j} ")

# n = 1 and j = 4 
# n = 1 and j = 5
# n = 2 and j = 4
# n = 2 and j = 5
```

### Challenge : Trace Your Investments

```
In this challenge, you will write a program called invest.py that tracks the
growing amount of an investment over time.
An initial deposit, called the principal amount, is made. Each year, the
amount increases by a fixed percentage, called the annual rate of return.
For example, a principal amount of $100 with an annual rate of return of
5% increases the first year by $5. The second year, the increase is 5% of the
new amount $105, which is $5.25.
Write a function called invest with three parameters: the principal amount,
the annual rate of return, and the number of years to calculate. The function
signature might look something like this:

def invest(amount, rate, years):

The function then prints out the amount of the investment, rounded to 2
decimal places, at the end of each year for the specified number of years.
```
```
def inverst (amount, rate, years):
    for n in range(years):
        amount = amount + (amount * rate)
        print("Year {} : ${:.2f}" .format((n+1), amount))
inverst(100, .05, 4)

# Year 1 : $105.00
# Year 2 : $110.25
# Year 3 : $115.76
# Year 4 : $121.55
```

### Understand Scope in Python
```
x = "Hello World"

def func():
    x = 3
    print("Inside 'func', x has the value {}" .format(x))

func()

print("Outside 'func', x has the value {}" .format(x))

# Inside 'func', x has the value 3
# Outside 'func', x has the value Hello World
```

### Scope Resolution
```
x = 5

def outer_func():
    y = 3

    def inner_func():
        z = x + y
        return z

    return inner_func()

print(outer_func())
# 8
```

### The LEGB Rule
```
L : Local
E : Enclosing
G : Global
B : Built-in
```

### Break the Rules
```
total = 0

def add_to_total(n):
    total = total + n

add_to_total(5)

print(total)

> python .\first_letter.py
Traceback (most recent call last):
  File "D:\Projects_Python\Ebook\Python101Basics\first_letter.py", line 6, in <module>
    add_to_total(5)
  File "D:\Projects_Python\Ebook\Python101Basics\first_letter.py", line 4, in add_to_total
    total = total + n
            ^^^^^
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
```

```
total = 0

def add_to_total(n):
    global total
    total = total + n

add_to_total(5)

print(total)
# 5
```

## 7. Summary and Additional Resources
```
Python "FOR" Loops (Definite Iteration)
Python "WHILE" Loops (Indefinite Iteration)
```