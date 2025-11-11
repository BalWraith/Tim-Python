import os;os.system('cls')
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5) # String Concatenation

print("he's " "probably " "pining " "for the " "fjords") # Concatenation

print("Hello " * 5) # Repetition

#print("Hello " * 5 + 4) # TypeError: can only concatenate str (not "int") 
print("Hello " * (5 + 4)) # with parentheses it works

today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thur" in today) # False
print("parrot" in "fjord") # False






