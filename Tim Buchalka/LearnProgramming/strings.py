import os;os.system('cls')
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world") # string concatenation
greeting = "Hello"
name = "Michael"
print(greeting + name) # string concatenation #HelloMichael no (space)

# if we want a space, we can add that too
print(greeting + ' ' + name) # string concatenation #Hello Michael (space)

age = 24
print(age) # prints the integer 24

print(type(greeting)) # <class 'str'>
print(type(age)) # <class 'int'>

age = 33
print(f"{name} is {age} years old") 
print(type(age)) # <class 'str'>

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}") # f-string with formatting

pi = 22/ 7
print(f"Pi is approximately {pi:12.50f}") # f-string with formatting

