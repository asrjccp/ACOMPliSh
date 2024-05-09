import streamlit as st
st.set_page_config(
    page_title= "Python Fundamentals",
    initial_sidebar_state= "auto"
)
from cb_python import answer_python
st.title(":rainbow[Python Fundamentals]")

# Create 3 colums to divide the buttons equally
col1, col2, col3 = st.columns(3)
# Content to be shown in Column 1
with col1:
    datatypes = st.button("Printing & Data Types")
    variables = st.button("Variables")
with col2:
    lists = st.button("CRUD with Lists")
    control = st.button("Control Statements")
with col3:
    loops = st.button("Loops")
    functions = st.button("Functions")
# --- Button 1 ---
if datatypes:
    st.markdown("**:blue[Printing]**")
    st.markdown('''
    * We will need to print the output of any code to have a solid understanding of what is happening behind the scenes to catch problems
    
    In Python, we would use the `print()` function to do so:
    ```python
                print("Hello World")
    ```         
''')
    st.markdown("**:blue[Data Types]**")
    st.markdown("**:red[Strings]**")
    st.markdown("Strings are sequence of characters enclosed with either single inverted commas ('') or double inverted commas (\"\")")
    st.markdown("These are the examples of strings")
    st.markdown("`'Hello World'`")
    st.markdown("`'123'`")
    st.markdown("We will not being able to carry out any calculations when you :red[**define numbers as a string**]")
    st.markdown(":red[**Integers**]")
    st.markdown("Integers are whole numbers **without decimal points** which can be either postive or negative")
    st.markdown("These are examples of integers")
    st.markdown("`123`")
    st.markdown("`-456`")
    st.markdown("**:red[Lists]**")
    st.markdown("Lists are a collection of items that are ordered (accessible) and mutable (changable)")
    st.markdown("Lists can contain elements of different data types and its elements are enclosed in [] square brackets separated by commas")
    st.markdown("These are the examples for lists")
    st.markdown("`[1, 2, 3]`")
    st.markdown("`[ABC, 88, DEF, 99]`")
    st.markdown("**:red[Dictionaries]**")
    st.markdown("Dictionaries are a collection of key-value pairs similar to the real world dictionary")
    st.markdown("The `key` is similar to the unique `word` in a dictionary and the `value` represents the meaning of the word")
    st.markdown("Dictionaies is defined with curly braces {} with its different keys separated by commas")
    st.markdown("Here are some examples of a dictionary")
    st.markdown('`{"A" : 99, "B": 55, "C": 72}`')
    st.markdown('`{"Singaporeans" : 50, "Malaysians": 50 }`')
    st.markdown(":red[**Booleans**]")
    st.markdown("Booleans represents either true or false values ")
    st.markdown('If we are converting an integer to a boolean, any non-zero number will be evaluated to `True` and zero values would be evaluated to `False`')
    st.markdown('These are the booleans in Python (take note of capitalisation!)')
    st.markdown('`True`')
    st.markdown('`False`')
# --- Button 2 ---
if variables:
    st.markdown(":blue[**Why Variables?**]")
    st.markdown("We can assign the values of different datatypes into a variable to :red[**prevent repeating ourselves**]")
    st.markdown("For example, if we are planning to use our full name many times in our code, we can assign it to a variable `name` and use it")
    st.markdown(":blue[**Rules for defining variables**]")
    st.markdown("* Variable names **:red[cannot start with numbers or special characters excluding underscores]**")
    st.markdown("* You cannot use :red[**spaces**] when defining the variable and would need to use _ to replace it")
    st.markdown("* Use meaningful variable names for others to understand. For example, do not use the variable name `age` to represents a person name")
    st.markdown("* Variables are case sensitive. `Name` and `name` are treated as different variables")
    st.markdown(":blue[**Examples of Variable Names**]")
    st.markdown(":green[**Valid:**]")
    st.markdown("`C0mputing`")
    st.markdown("`i_love_computing`")
    st.markdown("`_computing`")
    st.markdown(':red[**Invalid:**]')
    st.markdown("`1love`")
    st.markdown("`i love computing`")
    st.markdown(":blue[**Defining Variables:**]")
    st.markdown("To assign a value to a variable, we use the `=` sign")
    st.markdown('`name = "Computing Kid"` (string)')
    st.markdown('`age = 88` (integer)')
    st.markdown('`hobbies = ["coding", "eating", "sleeping"]` (list)')
    st.markdown('`adult = True` (boolean)')
    st.markdown("**:blue[Printing with Variables]**")
    st.markdown("From Python 3.6 (A-Level Version), we can use `print(f'')` to conscisely combine variables together")
    st.markdown("Let us define some variables and use `print(f'')` to print all of them in one statement")
    st.markdown('''
    ```python 
                name = "Computing Pro"
       age - 88
       hobbies = ['lim kopi', 'jiak beng']
       print(f"Hi, I am {name} and am now {age}. My hobbies are {hobbies}")         
    ```
    ```
    Output: Hi, I am Computing Pro and am now 88. My hobbies are ['lim kopi', 'jiak peng']
    ```
''')
    st.markdown("Hmm... The hobbies are still in the list format! We will solve this in the section of `CRUD with Lists`")
# --- Button 3 ---
if lists:
    # CREATE
    st.markdown(":blue[**1. Creating a List**]")
    st.markdown("We can initialise a list with square brackets ([]) with all of the elements separated by commas")
    st.markdown("Let's define a list named hobbies:")
    st.markdown("`hobbies = ['basketball', 'badminton', 'bowling']`")
    # Zero-Based Indexing
    st.markdown(":blue[**2. Zero-Based Indexing**]")
    st.markdown("You can think that all of the elements are given index numbers for us to easily access the elements")
    st.markdown("The first element is given the :red[**index of zero!**] instead of one")
    # Reading List
    st.markdown(":blue[**3. Reading a List**]")
    st.markdown("To access the first element of the list, we will access it with its variable name followed by square brackets containing its index")
    st.markdown("`print(hobbies[0])`")
    st.markdown('Output: `basketball`')
    st.markdown("To access the last element of the list:")
    st.markdown("`print(hobbies[2])`")
    st.markdown('Output: `bowling`')
    st.markdown("We can also **use negative indexing** to access elements from the back of the list")
    st.markdown("The last element of the list is given the value of `-1`")
    st.markdown("To access the last element of the list with negative indexing:")
    st.markdown("`print(hobbies[-1])`")
    st.markdown("Output: `bowling`")
    # Updating Lists
    st.markdown("**:blue[4. Updating a List]**")
    st.markdown(":blue[**4a.Append: Add element to the back of the list**]")
    st.markdown("We can add an element at the end of the list by using the `.append` method")
    st.markdown("To add a new hobby in the `hobbies` list:")
    st.markdown("`hobbies.append('skating')`")
    st.markdown("Now when we print out hobbies:")
    st.markdown("`print(hobbies)`")
    st.markdown("Output: `['basketball', 'badminton', 'bowling', 'skating']`")
    st.markdown("**:blue[4b. Insert: Add an element into our list with an arbitary index]**")
    st.markdown("We can apply the `.insert()` method with two arguments: `index` and `value`")
    st.markdown("We can add skating to the front of our list in this manner:")
    st.markdown('''
```python
hobbies = ['basketball', 'badminton', 'bowling']
hobbies.insert(0, 'skating')
print(hobbies)
```
''')
    st.markdown("Output: `['skating', 'basketball', 'badminton', 'bowling']`")
    st.markdown("**:blue[5. Delete]**")
    st.markdown("**:blue[5a. Pop - Remove last element of the list]**")
    st.markdown("We can use the `pop` method in order to remove the last element of the list")
    st.markdown("Given a list hobbies:")
    st.markdown('''
```python
hobbies = ['basketball', 'badminton', 'bowling']
hobbies.pop()
print(hobbies)              
```''')
    st.markdown("Output: `['basketball', 'badminton']`")
    st.markdown("**:blue[5b. Remove - Remove an element based on its value]**")
    st.markdown("Given a known value, we can remove that element with the `.remove()` method")
    st.markdown('''
```python
hobbies = ['basketball', 'badminton', 'bowling']
hobbies.remove('basketball')
print(hobbies)              
```''')
    st.markdown("Output: `['badminton', 'bowling]`")
    st.markdown("**:blue[5c. del - Remove an element based on its index]**")
    st.markdown("Given a known index, we can remove that element with the `del` keyword in this format")
    st.markdown("For example, to remove the second element of `hobbies` below")
    st.markdown('''
```python
hobbies = ['basketball', 'badminton', 'bowling']
del hobbies[1] # Recall Zero-Based Indexing
print(hobbies)              
```''')
    st.markdown("Output: `['basketball', 'bowling']`")
# --- Button 4 (If) ---
if control:
    st.markdown(":blue[**Condition Testing**]")
    st.markdown("We can control what the next step in any program with conditions which will evaluate to either `True` or `False` (boolean values)")
    st.markdown("Here is how we test conditions in Python")
    st.markdown('''
```
> : Greater
>= :Greater than or equal to
< : Lesser than
<= : Lesser than or equal to
!=: not equal to
== : equal to
''')
    st.markdown("Let's print the output of the following conditions: ")
    st.markdown('''
```python
print(20 == 40)
print(20 != 40)
print(20 > 40)
print(20 < 40)
''')
    st.markdown("**Output:**")
    st.markdown('''
```python
False
True
False
True
''')
    st.markdown("**:blue[If Statements]**")
    st.markdown("Here is the syntax of using `if` statements")
    st.markdown('''
```python
if condition:
    ...code...
''')
    st.markdown(":red[**Notice the indentation (either 2 or 4 spaces) after the colon**]")
    st.markdown("Let us try an example by testing if the person age is greater than 18")
    st.markdown('''
```python
age = 18
if age >=18:
    print("You are of age!")
''')
    st.markdown("Output: `You are of age!`")
    st.markdown(':blue[**If-Else Statements**]')
    st.markdown('We can also use `else` to execute some other code when none of the conditions in the control block is fulfilled')
    st.markdown('''
```python
age = 18
if age >=18:
    print("You are of age!")
else:
    print("You are not of age to enter")
''')
    st.markdown("Output: `You are not of age to enter`")
    st.markdown(":blue[**If-Elif-Else Statements**]")
    st.markdown("If we can test multiple conditions with the `elif` statements if the first condition is not fulfilled")
    st.markdown("We will be printing an error when the age inputted is negative here and **it is used in between `if` and `else`")
    st.markdown('''
```python
age = -5
if age >=18:
    print("You are of age!")
elif age <= 0:
    print("You entered an invalid age")
else:
    print("You are not of age to enter")
''')
    st.markdown("Output: `You entered an invalid age`")
if loops:
    st.markdown(":blue[**For Loops**]")
    st.markdown("Some tasks are repetitive in programming and a loop will help us do a task until a condiiton is fulfilled")
    st.markdown("Some other time, we will also want to iterate through our lists & dictionaries")
    st.markdown("**For Loop Syntax**")
    st.markdown('''
```python
for variable in iterable:
  Execute this block of code
```
`Variable` can be named anything you want, but the common names are `i`, `x` or `_`

`Iterable` are objects which can return its member one at a time (e.g. strings, list, dictionary)

''')
    st.markdown("Given a list of fruits, we can print out every element of the list with a `for` loop")
    st.markdown('''
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
''')
    st.markdown("**Output:**")
    st.markdown('''
```python
apple
banana
cherry
''')
    st.markdown("We can also loop through a dictionary (which contains key value pairs) with a slightly modified for loop")
    st.markdown('''
```python
grades = {'A': 50, 'B': 20}
for key, value in grades.items():
    print(f"The amoung of people who got {key} is {value}")
''')
    st.markdown('''
```python
The amount of people who got A is 50
The amount of people who got B is 20
''')
    st.markdown('Here we specify **2** arbitary variables to represent the `key` and `value` for every iteration of the loop')
    st.markdown('In the first iteration of the loop, `key` holds the value `A` while `value` holds the value `50`')
    st.markdown('In the second iteration of the loop, `key` holds the value of `B` while `value` holds to `value` of `20`')
    st.markdown(":blue[**While Loop**]")
    st.markdown("If we want to run some code until a condition is fulfilled, we can use `while` loop")
    st.markdown('''
```python
while condition:
    Execute some code
''')
    st.markdown("**Syntax**")
    st.markdown('''
```python
counter = 1
while counter < 5:
    print(counter)
    counter += 1
```
''')
    st.markdown("**Output:**")
    st.markdown('''
```python
1
2
3
4
```
''')
if functions:
    st.markdown(":blue[**Functions**]")
    st.markdown("When we need to perform a same task over and over again, we can reduce duplication in our code base with functions")
    st.markdown("To define a function, we can use the `def` keyword and pass in parameters which needs to be used in the function")
    st.markdown("**Syntax:**")
    st.markdown('''
```python
def function_name(param1, param2):
    <code here>
    return <variable>
```
''')
    st.markdown("For example we can write a function called `add_ten` which adds 10 to a number passed to it")
    st.markdown('''
```python
def add_ten(number):
    return number + 10
''')
    st.markdown("We can now use the function and print the result in this manner:")
    st.markdown("`print(add_ten(5)`")
    st.markdown("**Output**: `15`")
st.divider()
# Initialise a state to keep track of person response"
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_box = st.chat_input("Enter your question")
if chat_box:
    with st.chat_message("user"):
        st.markdown(chat_box)
    st.session_state.messages.append({"role": "user", "content": chat_box})
    response = answer_python(chat_box)
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})







