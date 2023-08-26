# String and String Methods

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

## 5. Challenge : Pick Adart Your User's Input

```
Write a script named first_letter.py that first prompts the user for input by using
the string "Tell me your password:" The script should then determine the first letter
of the user’s input, convert that letter to upper-case, and display it back.
```

```
response = input("Tell me your password : ")

response = response[0].upper() + response[1:]

print("The firstt letter you entered was : ", response)
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