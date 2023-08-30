# Function and Loopes

```
In this chapter, you will learn:
- How to create user-defined functions
- How to write for and while loops
- What scope is and why it is important
```
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

```
The process for executing a function can be summarized in 3 steps:
1. The function is called , and any arguments are passed to the function as input.
2. The function executes , and some action is performed with the arguments.
3. The function returns , and the original function call is replaced with the return value.
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

```
Every function has two parts:
1. The function signature defines the name of the function and any inputs it expects.
2. The function body contains the code that runs every time the function is used.
```

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

### Review Exercises

```
1. Write a function called cube () with one number parameter and returns the value of that number raised to the third power. Test the function by displaying the result of calling your cube () function on a few different numbers.
2. Write a function called greet () that takes one string parameter called name and displays the text "Hello <name>!" , where <name> is replaced with the value of the name parameter.
```

## 3. Challenge : Convert Temperatures
```
Write a script called temperature.py that defines two functions:

1. convert_cel_to_far() which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:

F = C * 9/5 + 32


2. convert_far_to_cel() which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:

C = (F - 32) * 5/9
```

## 4. Report a Block of Code

### The while Loop

```
There are two parts to every while loop:
1. The while statement starts with the while keyword, followed by a test condition , and ends with a colon (:).
2. The loop body contains the code that gets repeated at each step of the loop. Each line is indented four spaces.
```

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
Like its while counterpart, the for loop has two main parts:
1. The for statement begins with the for keyword, followed by a membership expression , and ends in a colon (:)
2. The loop body contains the code to be executed at each step of the loop, and is indented four spaces.
```

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

### Review Exercises
```
1. Write a for loop that prints out the integers 2 through 10, each on a new line, by using the range() function.
2. Use a while loop that prints out the integers 2 through 10 (Hint: you’ll need to create a new integer first)
3. Write a function called doubles() that takes one number as its input and doubles that number. Then use the doubles() function in a loop to double the number 2 three times, displaying each result on a separate line. Here is some sample output:
    4
    8
    16
```

## 5. Challenge : Trace Your Investments

```
In this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.

An initial deposit, called the principal amount, is made. Each year, the amount increases by a fixed percentage, called the annual rate of return.

For example, a principal amount of $100 with an annual rate of return of 5% increases the first year by $5. The second year, the increase is 5% of the new amount $105, which is $5.25. Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of years to calculate. The function
signature might look something like this:

def invest(amount, rate, years):

The function then prints out the amount of the investment, rounded to 2 decimal places, at the end of each year for the specified number of years.

For example, calling invest(100, .05, 4) should print the following:
year 1: $105.00
year 2: $110.25
year 3: $115.76
year 4: $121.55

To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years. Then call invest() to display the calculations for the values entered by the user.
```

## 6. Understand Scope in Python
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

### Additional Resources
```
Python "FOR" Loops (Definite Iteration)
Python "WHILE" Loops (Indefinite Iteration)
```