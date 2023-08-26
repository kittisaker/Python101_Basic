# Numbers and Math

## 1. Integer and Floating-Point Numbers

```
In this chapter, you will learn how to:
- Work with Python's three built-in nujber types: integer, floating-point and complex numbers
- Round numbers to a given number of decimal places
- Format and display numbers in strings
```

### Integer

```
>>> type(1)
<class 'int'>

>>> int("23")
23

>>> 1234
1234

>>> 1_234
1234
```

### Floating-Point Numbers

```
>>> type(1.0)
<class 'float'>

>>> float("1.54")
1.54

>>> 1_000.0
1000.0

>>> 1e6
1000000.0

>>> 2e+17
2e+17

>>> 1e-4
0.0001

>>> 2e400
inf

>>> type(2e400)
<class 'float'>

>>> -2e400
-inf
```

## 2. Arithmetic Operators and Expressions

### Addition
```
>>> 1 + 2
3

>>> 1.0 + 2
3.0
```

### Subtraction
```
>>> 1 - 1
0

>>> 5.0 - 3
2.0

>>> -3
-3

>>> 1- -3
4

>>> 1 - (-3)
4
```

### Multiplication

```
>>> 3 * 3
9

>>> 2 * 8.0
16.0
```

### Division

```
>>> 9/3
3.0

>>> int(9/3)
3
```

### Integer Division
```
>>> 9/3
3.0

>>> 9//3
3

>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### Exponents
```
>>> 2 ** 2
4

>>> 2 ** -2 
0.25
```

### The Modulus Operator
```
>>> 5 % 3
2
```

### Arithmetic Expressions
```
*, /, //, %, +, -
```

## 3. Challenge : Perform Calculations on User Input
```
Write a script called exponent.py that receives two numbers from the user and
displays the first number raised to the power of the second number.

Enter a base: 1.2
Enter an exponent: 3
1.2 to the power of 3 = 1.7279999999999998
```

## 4. Make Python Lie to You

```
>>> 0.1 + 0.2
0.30000000000000004
```

## 5. Math Functions and Number Methods

### The round() function

```
>>> round(2.3)
2
>>> round(2.7)
3
>>> round(3.7)
4
>>> 
```

```
>>> round(3.14159, 3)
3.142
>>> round(2.71828, 2)
2.72
```
### The abs() Function
```
>>> abs(3)
3

>>> abs(-5.0) 
5.0
```


### The pow() Function

```
>>> pow(2, 3)
8
>>> pow(2, -2)
0.25

# (x ** y) % z
>>> pow(2, 3, 2)
0
```

### Check if a Float Is Integral
```
>>> num = 2.5
>>> num.is_integer()
False

>>> num = 2.0
>>> num.is_integer()  
True
```

## 6. Print Numbers in Style
```
>>> n = 7.125

>>> f"The value of n is {n:.2f} "
'The value of n is 7.12 '

>>> print("The value of n is {:.2f} " .format(n))   
The value of n is 7.12
```

```
>>> n = 123456789

>>> f"The value of n is {n:,} "
'The value of n is 123,456,789 '

>>> print("The value of n is {:,} " .format(n))   
The value of n is 123,456,789
```

```
balance = 2000.0
spent = 256.35

balance = balance - spent

print("After spending $ {:,.2f} , I was left with $ {:,.2f} " .format(spent, balance))
```

```
>>> ratio = 0.9
>>> f"Over {ratio:.1%} of Pythonistas say 'Digital Academy rocks!'" 
"Over 90.0% of Pythonistas say 'Digital Academy rocks!'"
>>> f"Over {ratio:.2%} of Pythonistas say 'Digital Academy rocks!'" 
"Over 90.00% of Pythonistas say 'Digital Academy rocks!'"
```

## 7. Complex Numbers

```
>>> n = 1 + 2j 
>>>n
(1+2j)

>>>n.real
1.0

>>> n.imag
2.0

>>> n.conjugate()
(1-2j)
```

```
>>> a = 1 + 2j
>>> b = 3 - 4j

>>> a + b
(4-2j)

>>> a - b
(-2+6j)

>>> a * b
(11+2j)

>>> a ** b
(932.1391946432212+95.9465336603415j)

>>> a / b
(-0.2+0.4j)

>>> a // b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
```

```
>>> x = 42
>>> x.real
42
>>> x.imag
0
>>> x.conjugate()
42

>>> y = 3.14
>>> y.real
3.14
>>> y.imag
0.0
>>> y.conjugate()
3.14
```

## 8. Summary and Additional Resources

### Basic Data ypes in Python

#### Intergers

```
# Prefix
0b
0B

0o
0O

0x
0X
```

```
>>> 10
10
>>> 0x10
16
>>> 0b10
2

>>> type(10)
<class 'int'>
>>> type(0o10)
<class 'int'>
>>> type(0b10)
<class 'int'>
```

#### Floating-Point Numbers
```
>>> 4.2
4.2
>>> type(4.2)
<class 'float'>
>>> 4.
4.0
>>> .2
0.2
>>> .4e7
4000000.0
>>> 4.2e-4
0.00042
```

```
# Deep Dive: Floating-Point Representation
>>> 1.79e308
1.79e+308
>>> 1.8e308  
inf

>>> 5e-324
5e-324
>>> 1e-325
0.0
```

#### Complex Numbers
```
>>> type(2+3j)
<class 'complex'>
```

#### String
```
>>> print("I am a string.")
I am a string.
>>> print('I am too')       
I am too
```

```
>>> print('This string contains a single quote (\') character.')
This string contains a single quote (') character.
```

```
# Escape Sequence
>>> print('a\
... b\
... c')
abc

>>> print('foo\\bar')
foo\bar

>>> print('foo\tbar')
foo     bar
```

```
# Escape Sequence
>>> print("a\tb")
a       b
>>> print("a\141\x61")
aaa

>>> print("a\nb")
a
b

>>> print('\u2192 \N{rightwards arrow}') 
→ →
```

```
# Raw String 
>>> print('foo\nbar')
foo
bar

>>> print(r'foo\nbar')
foo\nbar

>>> print(R'foo\nbar') 
foo\nbar
```

```
# Triple-Quoted Strings

>>> print("""This is a 
... string that spans
... across several lines""")
This is a
string that spans
across several lines
```


#### Boolean Type, Boolean Context, and “Truthiness”

```
>>> type(True)  
<class 'bool'>
>>> type(False) 
<class 'bool'>

```


#### Built-In Functions

```
# Math
abs()
divmod()
max()
min()
pow()
round()
sum()
```

```
# Type Conversion
ascii()
bin()
bool()
chr()
complex()
float()
hex()
int()
oct()
ord()
repr()
str()
type()
```

```
# Iterables and Iterators
all()
any()
enumerate()
filter()
iter()
len()
map()
next()
range()
reversed()
slice()
sorted()
zip()
```

```
# Composite Data Type
bytearray()
bytes()
dict()
frozenset()
list()
object()
set()
tuple()
```

```
# Classes, Atrributes, and Inheritance
classmethod()
delattr()
getattr()
hasattr()
isinstance()
issubclass()
property()
setattr()
super()
```

```
# Input / Output
format()
input()
open()
print()
```

```
# Variables, References, and Scope
dir()
globals()
id()
locals()
vars()
```

```
# Miscellaneous
callable()
compile()
eval()
exec()
hash()
help()
memoryview()
staticmethod()
__import__()
```


### How to Round Numbers in Python

#### Python's Built-in round() Function
```
>>> round(2.5)
2
>>> round(1.5) 
2
```

#### How much Impact Can Rounding Have?
```
import random
random.seed(100)

def truncate(n):
    return int(n * 1000) / 1000

actual_value, truncated_value = 100, 100

for _ in range(1_000_000):
    delta = random.uniform(-0.05, 0.05)
    actual_value = actual_value + delta
    truncated_value = truncate(truncated_value + delta)

print(actual_value)

print(truncated_value)

> python .\first_letter.py
96.45273913513529
0.239
```

```
import random
random.seed(100)

def truncate(n):
    return int(n * 1000) / 1000

actual_value, rounded_value = 100, 100

for _ in range(1_000_000):
    delta = random.uniform(-0.05, 0.05)
    actual_value = actual_value + delta
    rounded_value = round(rounded_value + delta, 3)

print(actual_value)

print(rounded_value)

> python .\first_letter.py
96.45273913513529
96.258
```

#### Basic but Biased Roundind Strategies

```
# Truncating

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

print(truncate(12.5))

print(truncate(-5.963, 1))

print(truncate(1.625, 2))

print(truncate(125.6, -1))

print(truncate(-1374.25, -3))

# 2.0
# -5.9
# 1.62
# 120.0
# -1000.0
```

```
# Rounding Up
import math

print(math.ceil(3.7))
print(math.ceil(2))
print(math.ceil(-0.5))
# 4
# 2
# 0

import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

print(round_up(1.1))
print(round_up(1.23, 1))
print(round_up(1.543, 2))
print(round_up(22.45, -1))
print(round_up(1352, -2))
print(round_up(-1.5))

# 2.0
# 1.3
# 1.55
# 30.0
# 1400.0
# -1.0
```

```
# Rounding Down
import math

print(math.floor(1.2))
print(math.floor(-0.5))
# 1
# -1

import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

print(round_down(1.5))
print(round_down(1.37, 1))
print(round_down(-0.5))
# 1.0
# 1.3
# -1.0
```

#### Interlude: Rounding Bias

```
import statistics

numbers = [1.25, -2.67, 0.43, -1.79, 8.19, -4.32]
print(statistics.mean(numbers))
# 0.18166666666666653
```

rounding.py
```
import math

def truncate(n, decimals=0):
    multiplier = 10**decimals
    return int(n * multiplier) / multiplier

def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier

def round_down(n, decimals=0):
    multiplier = 10**decimals
    return math.floor(n * multiplier) / multiplier
```

```
import statistics
from rounding import truncate, round_up, round_down

numbers = [1.25, -2.67, 0.43, -1.79, 8.19, -4.32]

print(statistics.mean(numbers))

print([truncate(n, 1) for n in numbers])

print(statistics.mean([truncate(n, 1) for n in numbers]))

print(statistics.mean([round_up(n, 1) for n in numbers]))

print(statistics.mean([round_down(n, 1) for n in numbers]))

# 0.18166666666666653
# [1.2, -2.6, 0.4, -1.7, 8.1, -4.3]
# 0.1833333333333333
# 0.23333333333333325
# 0.13333333333333316
```

#### Better Rounding Strategies in Python

Rounding Half Up

rounding.py
```
...
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier
```

```
from rounding import round_half_up

print(round_half_up(1.23, 1))

print(round_half_up(1.28, 1))

print(round_half_up(1.25, 1))

print(round_half_up(-1.5))

print(round_half_up(-1.25, 1))

print(round_half_up(2.5))

print(round_half_up(1.225, 2))

# 1.2
# 1.3
# 1.3
# -1.0
# -1.2
# 3.0
# 1.23
```

```
>>> -1.225 * 100
-122.50000000000001
>>> _ + 0.5
-122.00000000000001
>>> import math
>>> math.floor(_)
-123
>>> _ / 100
-1.23
```

Rounding Half Down

rounding.py
```
...
def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier - 0.5) / multiplier
```

```
https://realpython.com/python-rounding/
```