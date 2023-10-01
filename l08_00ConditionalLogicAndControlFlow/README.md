# Conditional Logic and Control Flow

```
In this chapter, you will learn how to :
- Compare the values of two or more variables
- Write if statements to control the flow of your programs
- Handle errors with try and except
- Apply conditional logic to create simple simulations
```

## 1. Compare Values (>, <, >=, <=, !=, ==)

```
Ex
>>> "a" == "a"
True
>>> "a" == "b"
False
>>> "a" < "b"
True
>>> "apple" < "atari"
True
```

### Review Exercises

```
1. For each of the following conditional expressions, guess whether they evaluate to True or False . Then type them into the interactive window to check your answers:
    1 <= 1
    1 <= 1
    1 != 2
    "good" != "bad"
    "good" != "Good"

2. For each of the following expressions, fill in the blank (indicated by ….. ) with an appropriate Boolean comparator so that the expression evaluates to True :
    3 ….. 4
    10 ….. 5
    "jack" ….. "jill"
    42 ….. "42"
```

## 2. Add Some Logic

### The "and" Keyword
```
>>> 1 < 2 and 3 < 4
True
```

### The "or" Keyword
```
>>> 1 < 2 or 3 < 4
True
```

### The "not" Keyword
```
>>> not True
False
>>> not False
True
```

```
Operator Precedence (Highest to Lowest)
<
<=
==
>=
>
not
and
or
```

```
>>> not False
True
>>> False == not True
  File "<stdin>", line 1
    False == not True
             ^^^
SyntaxError: invalid syntax

>>> False == (not True)
True
```

### Building Complex Expressions
```
>>> True and not (1 != 1)
True
>>> True and not (False)
True

>>> ("A" != "A") or not (2 >= 3)
True
```

```
>>> True and False == True and False
False

>>> (True and False) == (True and False)
True
```

### Review Exercises

```
1. Figure out what the result will be ( True or False ) when evaluating the following expressions, then type them into the interactive window to check your answers:
    (1 <= 1) and (1 != 1)
    not (1 != 2)
    ("good" != "bad") or False
    ("good" != "Good") and not (1 == 1)

2. Add parentheses where necessary so that each of the following expressions evaluates to True :
    False == not True
    True and False == True and False
    not True and "A" == "B"
    "B" and not "A" != "B"
```

## 3. Control the Flow of Your Program

### The if Statement
```
grade = 40

if grade >= 70:
    print("You passed the class!")

if grade < 70:
    print("You did not pass the class :( ")

print("Thank you for attending.")

# You did not pass the class :( 
# Thank you for attending.
```

### The else Keyword
```
grade = 40

if grade >= 70:
    print("You passed the class!")
else :
    print("You did not pass the class :( ")

print("Thank you for attending.")

# You did not pass the class :( 
# Thank you for attending.
```

### The elif Keyword
```
grade = 85

if grade >= 90:
    print("You passed the class with a A.")
elif grade >= 80:
    print("You passed the class with a B.")
elif grade >= 70:
    print("You passed the class with a C.")
else :
    print("You did not pass the class :( ")

print("Thank you for attending")

# You passed the class with a B.
# Thank you for attending
```

### Nested if Statement
```
sport = input("Enter a sport : ")
p1_score = input("Enter player 1 score : ")
p2_score = input("Enter player 2 score : ")

if sport.lower() == "basketball":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
elif sport.lower() == "golf":
    if p1_score == p2_score:
        print("The game is a draw.")
    elif p1_score < p2_score:
        print("Player 1 wins.")
    else:
        print("player 2 wins.")
else:
    print("Unknown sport.")

# Enter a sport : basketball
# Enter player 1 score : 5
# Enter player 2 score : 2
# Player 1 wins.
```

```
Sport               Score values
basketball          player1_score == player2_score
basketball          player1_score > player2_score
basketball          player1_score < player2_score
golf                player1_score == player2_score
golf                player1_score > player2_score
golf                player1_score < player2_score
everything else     any combination

We can describe this with compound conditional expressions:

p1_wins_basketball = sport == "basketball" and p1_score > p2_score
p1_wins_golf = sport == "golf" and p1_score < p2_score
p1_wins = player1_wins_basketball or player1_wins_golf

Now p1_wins will be True if player 1 wins the basketball game or the golf game, and will be False 
otherwise. Using this code, you can simplify the program quite a bit:
```

```
sport = input("Enter a sport : ")
p1_score = input("Enter player 1 score : ")
p2_score = input("Enter player 2 score : ")

if p1_score == p2_score:
    print("The game is a draw.")
elif sport.lower() == "basketball" or sport.lower() == "golf":
    p1_wins_basketball = sport == "basketball" and p1_score > p2_score
    p1_wins_golf = sport == "golf" and p1_score < p2_score
    p1_wins = p1_wins_basketball or p1_wins_golf

    if p1_wins:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")

# Enter a sport : basketball
# Enter player 1 score : 5
# Enter player 2 score : 2
# Player 1 wins.
```

## 4. Challenge : Find the Factors of a Number
```
# A factor of a positive integer n is any positive integer less than or equal to n that
# divides n with no remainder.
# For example, 3 is a factor of 12 because 12 divided by 3 is 4 , with no remainder.
# However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2
# .
# Write a script factors.py that asks the user to input a positive integer and then
# prints out the factors of that number. Here’s a sample run of the program with
# output:

# Enter a positive integer : 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12

n = int(input("Enter a positive integer : "))

for i in range(1, n+1):
    if(n % i == 0):
        print("{} is a factor of {} " .format(i, n))
```

## 5. Break Out of the Pattern

### if Statements and for Loops
```
sum_of_evens = 0

for n in range(1, 100):
    if n % 2 == 0:
        sum_of_evens = sum_of_evens + n
        print("... + {} = {}" .format(n, sum_of_evens))

# The final value of sum_of_evens is 2450
```

### The break Keyword
```
for n in range(0, 4):
    if n == 2:
        break

    print(n)

print("Finished with n = {} " .format(n))

# 0
# 1
# Finished with n = 2
```

### The continue Keyword
```
for i in range(0, 4):
    if i == 2:
        continue
    print(i)

print("Finished with n = {} " .format(i))

# 0
# 1
# 3
# Finished with n = 3
```

### for...else loops
```
phrase = "it marks the spot"

for character in phrase:
    print(character)
    if character == "s":
        break
else:
    print("there was no 'X' in the phrase")

# i
# t

# m
# a
# r
# k
# s
```

```
for n in range(3):
    password = input("Password : ")

    if password == "I<3Bieber":
        break
    
    print("Password is incorrect.")

else :
    print("Suspicious activity. The authorities have been alerted.")
```

## 6 Recover From Errors

### A Zoo of Exceptions

#### ValueError
```
in("not a number")
```

#### TypeError
```
"1" + 2
```

#### NumeError
```
print(does_not_exist)
```

#### ZeroDivisionError
```
1/0
```

#### OverflowError
```
pow(2.0, 1_000_000)
```

### The try and except Keywords
```
try:
    number = int(input("Enter an integer : "))

except ValueError:
    print("That was not an integer")
```

```
def divide(num1, num2):
    try:
        print(num1/num2)
    except(TypeError, ZeroDivisionError):
        print("encountered a problem")

result = divide(5, 0)
```

```
def divide(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Boat arguments must be numbers")
    except(TypeError, ZeroDivisionError):
        print("num2 must not be 0")

result = divide(3, 0)
```

### The "Bare" except Clause
```
try:
    # Do lots of hazardous things that might break
except:
    print("Something bad happened!")
```