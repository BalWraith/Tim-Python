import os;os.system('cls')
# age = int(input("How old are you? "))
# # if age >= 16 and age <= 65: # age is Greater or equal to 16 and age is less than or equal to 65
# if 16 <= age <= 65: # age = 16-65 same as the above ^^^^ without (and)
#     print("Have a good day at work")
# else:
#     print("Enjoy your free time")

# print("-" * 80)

# if age < 16 or age > 65: # Only one has to be right
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

age = int(input("How old are you? "))
if age not in range(16,66):
    print("Enjoy your free time")
else:
    print("Have a good day at work") 




    
    
