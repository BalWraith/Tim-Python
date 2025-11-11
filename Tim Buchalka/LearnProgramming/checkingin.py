parrot = "Norwegian Blue"     ;import os;os.system('cls')

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't neet that letter")

