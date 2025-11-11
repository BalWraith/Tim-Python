# import os;os.system('cls')
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:# this block will add non numbers to the variable separators
    if not char.isnumeric():# .isnumeric() - what is vs whats not a number
        separators = separators + char# adds what are not number to the separators variable 
# print(separators)



values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))# with sum will add all numbers inputted with a separator EX:(1;5;6[9]5 = 26)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])# this will format separators into a , EX:(1;5;6[9]5 = [1, 5, 6, 9, 5] )





# number = "9,223;372:036 854,775;807"
# seperators = number[1::4]
# print(seperators) # ,;: ;,;
# values = "".join(char if char not in seperators else " " for char in number).split() #changes all seperators(,;:) to space then splits ['9', '223', '372', '036', '854', '775', '807']
# print([int(val) for val in values]) # [9, 223, 372, 36, 854, 775, 807]# takes values for the above code and converts all to int