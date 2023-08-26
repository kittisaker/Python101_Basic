# String and String Methods

```
In this chapter, you will learn how to:
- Manipulate string with string methods
- Work with user input
- Deal with strings of numbers
- Format strings for printing
```

## 1. What is a String?

### The String Data Type

```
>>> type("Hello, World")
<class 'str'>
```

```
>>> test = "Hello World"
>>> type(test)
<class 'str'>
```

### String Literals
```
>>> string1 = "Hello World"
>>> string2 = "1234"
```

### Determine the Length of a String

```
>>> len("abc")
3
```

```
>>> letters = "abc"
>>> num_letters = len(letters)
>>> num_letters
3
```

### Multiline String

```
>>> paragraph = "sfdsgdgdf;dkaf;kjas;jf;jak;as;fa; \
... slfkdsgksjf;skakakjd;jfkadfnkdsnfkjsad;fkja;kfd;f\
... urwiewujsn onfnodn ndvkjo jodjdwoi hlihdhfhsdjkojhw\
... dfweioriwfhhguhghhfjkdfjdjhfhegkjdnemo  oefwofowf"

>>> print(paragraph)
sfdsgdgdf;dkaf;kjas;jf;jak;as;fa; slfkdsgksjf;skakakjd;jfkadfnkdsnfkjsad;fkja;kfd;furwiewujsn onfnodn ndvkjo jodjdwoi hlihdhfhsdjkojhwdfweioriwfhhguhghhfjkdfjdjhfhegkjdnemo  oefwofowf
```

```
>>> paragraph = """skdflkdgls;f;lksf;a;lf;ld
... slfj;sakjf;kj;aj;fkjd;kdsjf;aj;a;j;lajf;lkj
... ;dfjkjsda;fk;aka;j;a;a;;;a;kdf;sdkf;a;jaf """

>>> print(paragraph)
skdflkdgls;f;lksf;a;lf;ld
slfj;sakjf;kj;aj;fkjd;kdsjf;aj;a;j;lajf;lkj
;dfjkjsda;fk;aka;j;a;a;;;a;kdf;sdkf;a;jaf
```

### Review Excercises
```
1. Print a string that uses double quotation marks inside the string
2. Print a string that uses an apostrophe inside the string
3. Print a string that spans multiple line with whitespace preserved
4. Print a string that is codded on multiple lines but displays on a single line.
```

## 2. Concatenation, Indexing and Slicing

```
In this section, you'll learn about three basic string operations:
1. Concatenation, which joins two strings together
2. Indexing, which gets a single character from a string
3. Slicing, which gets several characters from a string at once
```

### String Concatenation
```
>>> string1 = "abc"
>>> string2 = "def" 
>>> magic_string = string1 + string2
>>> magic_string
'abcdef'

>>> magic_string = string1 + " " + string2  
>>> magic_string
'abc def'
```

### String Indexing
```
>>> flavor = "apple pie" 

>>> flavor[1]
'p'

>>> flavor[9] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> flavor[-1] 
'e'

>>> flavor[-10] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

```

```
>>> user_input = "kittisak"
>>> final_index = len(user_input) - 1
>>> final_index
7
>>> last_character = user_input[final_index]
>>> last_character
'k'
>>> print(user_input[-1])
k
```

### String Slicing
```
>>> test = "solo dev"

>>> first_three_letters = test[0] + test[1] + test[2]
>>> first_three_letters
'sol'
```

```
>>> test = "solo dev"

>>> test[0:3]
'sol'

>>> test[3:]
'o dev'

>>> test[:]  
'solo dev'

>>> test[:14] 
'solo dev'

>>> test[12:14] 
''

>>> test[-8 : -5] 
'sol'
```

### Strings Are Immutable
```
>>> word = "goal"

>>> word[0] = "f"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> word = "f" + word[1:]
>>> word
'foal'
```

### Review Exercises
```
1. Create a string and print its length using the len() function.
2. Create two string, concatenate them, and print the result.
3. Create two strind variables, then print one of them after the other (with a space added in between) using a comma in your print statement.
4. Repeat exercise 3, but instead of using commas in print(), use concatenation to add a space between the two strings.
5. Print the string "zing" by using slice notation on the string "bazinga" to specify the correct range of characters.

```

## 3. Manipulate Strings With Methods

```
In this section, you will learn how to:
- Convert a string to upper or lower case
- Remove white space from string
- Determine if a string begins and ends with certain characters
```

### Converting String Case

```
>>> "Solo Dev".lower()
'solo dev'

>>> "Solo Dev".upper() 
'SOLO DEV
```

### Removing Whitespace From a String

```
>>> " SOLO dev ".rstrip()
' SOLO dev'

>>> " SOLO dev ".lstrip() 
'SOLO dev '

>>> " SOLO dev ".strip()  
'SOLO dev'
```

### Determine if a String Starts or Ends With a Particular String

```
>>> "kittisak hanheam".startswith("kit")
True
>>> "kittisak hanheam".startswith("sd;fjd") 
False

>>> "kittisak hanheam".endswith("eam")      
True
>>> "kittisak hanheam".endswith("s;jfkd") 
False
```

### String Methods and Immutability

```
>>> name = "Kope"

>>> name.upper()
'KOPE'
>>> name
'Kope'

>>> name = name.upper() 
>>> name
'KOPE'
```

### Use IDLE to Discover Additional String Methods

```
>>> name = "Kope"
>>> name. // scroll through with the arrow keys.
```

### Review Exercises
```
1. Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each lowercase string on a separate line. Srting on a separate line.
2. Repeat Exercise 1, but convert each string to uppercase instead of lowercase.
3. Write a script that removes whitespace from the following strings. Print out the strings with the whitespace removed.
  string1 = " Filet Mignon"
  string2 = "Brisket "
  string3 = " Cheeseburger "
4. Write a script that prints out the result of .startswith("be") on each of the following strings:
  String1 = "Becomes"
  string2 = "becomes"
  string3 = "BEAR"
  string4 = " bEautiful"
  string4 = " beautiful"
5. Using the same four strings from Exercise 4, write a script that uses string methods to alter each string so that .startswith("be") returns True for all of them.
```

## 4. Interact With User Input

```
>>> prompt = "Hey, what's up? " 
>>> user_input = input(prompt)
Hey, what's up? I'm goods.

>>> print("You said : ", user_input)
You said :  I'm goods.
```

```
>>> response = input("What should I shout? ")
What should I shout? Noodle.

>>> response = response.upper()

>>> print("Well, if you insist...", response)
Well, if you insist... NOODLE.
```

### Exercises
```
1. Write a script that takes input from the user and displays that input back.
2. Write a script that takes input from the user and displays the input in lowercase.
3. Write a script that takes input from the user and displays the number of characters inputted.

```

## 5. Challenge : Pick Adart Your User's Input

```
Write a script named first_letter.py that first prompts the user for input by using
the string "Tell me your password:" The script should then determine the first letter
of the user’s input, convert that letter to upper-case, and display it back.
```

```
For example, if the user input is "no" then the program should respond like this:
The first letter you entered was: N
```

## 6. Working With String and Numbers

```
>>> str1 = "2"
>>> str1 + str1 
'22'

>>> str1 = "2"  
>>> str1 * 3    
'222'
>>> 3 * str1
'222'

>>> str1 * "3" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'

>>> str1 + 3  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

```
>>> num = input("Enter a number to be doubled : ")
Enter a number to be doubled : 5
>>> doubled_num = num * 2
>>> print(doubled_num)
55
```

```
>>> int("5")
5

>>> float("5")
5.0

>>> int("5.0")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '5.0'
```

```
>>> num = input("Enter a number to be doubled : ")
Enter a number to be doubled : 5.0
>>> doubled_num = float(num) * 2 
>>> print(doubled_num)
10.0
```

```
>>> str(print)
'<built-in function print>'
>>> str(int)
"<class 'int'>"
>>> str(float)
"<class 'float'>"
```

### Exercises
```
1. Create a string containing an integer, then convert that string into an actual integer object using int() . Test that your new object is a number by multiplying it by another number and displaying the result.
2. Repeat the previous exercise, but use a floating-point number and float() .
3. Create a string object and an integer object, then display them side- by-side with a single print statement by using the str() function.
4. Write a script that gets two numbers from the user using the input() function twice, multiplies the numbers together, and displays the result. If the user enters 2 and 4 , your program should
print the following text:
  The product of 2 and 4 is 8.0.
```


## 7. Streamline Your Print Statements

```
Suppose you have a string name = "Zaphod" and two integers heads = 2 and arms =
3 . You want to display them in the following line: Zaphod has 2 heads and 3 arms .
This is called string interpolation , which is just a fancy way of saying that
you want to insert some variables into specific locations in a string.
```

```
name = "Zaphod"
heads = 2
arms = 3

print(name, "has" ,str(heads), "heads and" ,str(arms), "arms")

# or

print(name+ " has " +str(heads)+ " heads and " +str(arms)+ " arms")

# or

print(f"{name} has {heads} heads and {arms} arms")
```

```
>>> n = 3
>>> m = 4
>>> f"{n} times {m} is {n * m}"  
'3 times 4 is 12'
```

```
name = "Zaphod"
heads = 2
arms = 3

print("{} has {} heads and {} arms" .format(name, heads, arms))
```
### Exercises

```
1. Create a float object named weight with the value 0.2, and create a string object named animal with the value " newt" . Then use these objects to print the following string using only string concatenation:
0.2 kg is the weight of the newt.
2. Display the same string by using the .format() method and empty {} place-holders.
3. Display the same string using an f-string.
```
## 8. Find a String in a String

```
>>> phrase = "the surprise is in here somewhere"       
>>> phrase.find("surprise")
4

>>> phrase.find("sfdfds")   
-1
```

```
>>> "solo dev".find("o")
1
```

```
>>> test = "solo dev"
>>> test.replace("dev", "Kope")
'solo Kope

>>> test
'solo dev'
```

## 9. Challenge : Turn Your User Into a L33t H4x0r

```
Write a script called translate.py that asks the user for some input with
the following prompt: Enter some text: . Then use the .replace() method to
convert the text entered by the user into “ leetspeak ” by making the
following changes to lower-case letters:
```

```
# a = 4
# b = 8
# e = 3
# l = 1
# o = 0
# s = 5

user_input = input("Enter some text: ")
modify1 = user_input.replace("a", "4")
modify1 = modify1.replace("b", "8")
modify1 = modify1.replace("e", "3")
modify1 = modify1.replace("l", "1")
modify1 = modify1.replace("o", "0")
modify1 = modify1.replace("s", "5")
modify1 = modify1.replace("t", "7")

print(modify1)

# Enter some text: I like to eat eggs and spam.
# I 1ik3 70 347 3gg5 4nd 5p4m.
```

<hr/>