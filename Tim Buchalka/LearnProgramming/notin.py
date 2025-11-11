import os;os.system('cls')
activity = input("What would you like to do today? ") 

if "cinema" not in activity.casefold():# casefold() makes (CINEMA and cinema) the same value 
    print("But I want to go to the cinema")
else:
    print("Ok")


