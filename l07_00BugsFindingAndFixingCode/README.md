# Bugs Finding & Fixing Code

## 1. Use the Debug Control Window
### The Debug Control Window : An Overview

```
# Debug > Degugger
for i in range(1, 4):
    j = i * 2
    print("i is {} and j is {}" .format(i, j))
```

### The Step Button

```
Click "Step" button
```

### Breakpoints and the "Go" Button
```
Go
```

### "Over" and "Out"
```
Over, Out
```

## 2. Squash Some Bugs
```
def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = word[i] + "_"
    return new_word

print(add_underscores("hello"))

# o_
```

```
1. Guess which section of code may contain the bug.
2. Set a breakpoint and inspect the code by stepping through the buggy section one line at a time, keeping track of important variables along the way.
3. Identify the line of code, if any, with the error and make a change to solve the problem.
4. Repeat steps 1–3 as needed until the code works as expected

```

### Step 1 : Make a Guess About Where the Bug Is Located

### Step 2 : Set a Breakpoint and Inspect the Code

### Step 3 : Identify the Error and Attempt to Fix It
```
new_word = word[i] + "_"
# change to
new_word = new_word + word[i] + "_"
```

```
def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
    return new_word

print(add_underscores("hello"))

# _h_e_l_l_o_
```

### Step 4 : Repeat Step 1-3 Until the Bug is Gone

### Alternative Ways to Find Mistakes in Your Code
```
def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = word[i] + "_"
        print("i = {} ; new_word = {}" .format(i, new_word)) # add...
    return new_word

print(add_underscores("hello"))

# i = 0 ; new_word = h_
# i = 1 ; new_word = e_
# i = 2 ; new_word = l_
# i = 3 ; new_word = l_
# i = 4 ; new_word = o_
# o_
```

```
def add_underscores(word):
    new_word = "_"
    for i in range(0, len(word)):
        new_word = new_word + word[i] + "_"
        print("i = {} ; new_word = {}" .format(i, new_word)) # add...
    return new_word

print(add_underscores("hello"))

# i = 0 ; new_word = _h_
# i = 1 ; new_word = _h_e_
# i = 2 ; new_word = _h_e_l_
# i = 3 ; new_word = _h_e_l_l_
# i = 4 ; new_word = _h_e_l_l_o_
# _h_e_l_l_o_
```

## 3. Summary and Additional Resources
```
1. Guess where the bug is located
2. Set a breakpoint and inspect the code
3. Identify the error and attempt to fix it
4. Repeat steps 1-3 until the error is fixed
```

---