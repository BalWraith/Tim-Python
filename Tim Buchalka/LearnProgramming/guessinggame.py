import os,random,string;os.system('cls')


def get_integer(prompt):
    """
    Gets an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered. 

    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))
        

help(get_integer)

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

highest = 1000
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
guess = 0
attemp = 0
while guess != answer:
    guess = get_integer(": ")

    if guess < answer:
       print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
        
if guess == answer and attemp == 1:
    print("You got it right the first time")
else:
    print("You got it right")
       




        






