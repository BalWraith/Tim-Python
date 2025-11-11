import os;os.system('cls')

name = "Michael" #input("Hello, what is your name? ")
age = int(input("What is your age? "))

if age >= 18 and age <= 30:# age is between 18-30
    print("Welcome {} you can come on holiday!".format(name))
elif age < 18:# age is under 18
    print("Sorry {} your too young wait another {} years".format(name, 18 - age))
else:# age is over 30
    print("Listen old man {} your {} years too late!".format(name, age - 30))







