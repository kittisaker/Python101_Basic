# Python Basic

## Chapter 4 : String and String Methods

In this chapter, you will learn how to:
* Manipulate string with string methods
* Work with user input
* Deal with strings of numbers
* Format strings for printing

### 1. What is a String?
* The String Data Type

```shell
>>> type("Hello, World")
<class 'str'>

>>> test = "Hello World"
>>> type(test)
<class 'str'>
```

* String Literals

```shell
>>> string1 = "Hello World"
>>> string2 = "1234"
```

* Determine the Length of a String
```shell
>>> len("abc")
3

>>> letters = "abc"
>>> num_letters = len(letters)
>>> num_letters
3
```

* Multiline String

```shell
>>> paragraph = "sfdsgdgdf;dkaf;kjas;jf;jak;as;fa; \
... slfkdsgksjf;skakakjd;jfkadfnkdsnfkjsad;fkja;kfd;f\
... urwiewujsn onfnodn ndvkjo jodjdwoi hlihdhfhsdjkojhw\
... dfweioriwfhhguhghhfjkdfjdjhfhegkjdnemo  oefwofowf"

>>> print(paragraph)
sfdsgdgdf;dkaf;kjas;jf;jak;as;fa; slfkdsgksjf;skakakjd;jfkadfnkdsnfkjsad;fkja;kfd;furwiewujsn onfnodn ndvkjo jodjdwoi hlihdhfhsdjkojhwdfweioriwfhhguhghhfjkdfjdjhfhegkjdnemo  oefwofowf
```

```shell
>>> paragraph = """skdflkdgls;f;lksf;a;lf;ld
... slfj;sakjf;kj;aj;fkjd;kdsjf;aj;a;j;lajf;lkj
... ;dfjkjsda;fk;aka;j;a;a;;;a;kdf;sdkf;a;jaf """

>>> print(paragraph)
skdflkdgls;f;lksf;a;lf;ld
slfj;sakjf;kj;aj;fkjd;kdsjf;aj;a;j;lajf;lkj
;dfjkjsda;fk;aka;j;a;a;;;a;kdf;sdkf;a;jaf
```

* Review Excercises
    1. Print a string that uses double quotation marks inside the string
    2. Print a string that uses an apostrophe inside the string
    3. Print a string that spans multiple line with whitespace preserved
    4. Print a string that is codded on multiple lines but displays on a single line.


### 2. Concatenation, Indexing and Slicing

In this section, you'll learn about three basic string operations:
1. Concatenation, which joins two strings together
2. Indexing, which gets a single character from a string
3. Slicing, which gets several characters from a string at once

* String Concatenation

```jshell
>>> string1 = "abc"
>>> string2 = "def" 
>>> magic_string = string1 + string2
>>> magic_string
'abcdef'

>>> magic_string = string1 + " " + string2  
>>> magic_string
'abc def'
```

* String Indexing
```jshell
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

```shell
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