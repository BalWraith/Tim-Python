import os;os.system('cls')
# %f for
# %d %s - displays whats in the () at the end of the string in the order it's in
# %x - displays numbers in hexadecimal 
# %o - displays # in octal format (o-7)

age = 24
# print("My age is %d years" % age ) # old style formatting 
# print("My age is {0}".format(age)) # use format method to insert integer into string
# print(f"My age is {age} years") # f-string, available in Python 3.6 and later

major = "years"
minor = "months"
print("My age is %d %s, %d %s" %(age, major, 6, minor))# replacement in order not based on letter 
print("PI is approcimately %60.50f" %(22/7)) # %60.50f 
