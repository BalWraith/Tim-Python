import os;os.system('cls')
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
# print(age)
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18: # GREATER THAN 18 BUT NOT 900
     print("Please come back in {0} years".format(18 - age))
     
elif age == 900: # EQUAL TO 900 ONLY
    print("Sorry, Yoda you die in Retrun of the Jedi")

else: # LESS THAN 18
    print("You are old enough to vote")
    print("Please put an X in the box")








    
    
