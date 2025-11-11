import os;os.system('cls')
# fizz = 3
# buzz = 5
# def fizz_buzz(x):
#     """
#     :param x: This number is used as a place holder for the value to be added later
#     :return: `fizz` i % 3 == 0
#             `buzz` i % 5 == 0
#             `fizz_buzz` i % 3 and i % 5 == 0
#     """
#     if x % 3 == 0 and x % 5 == 0:
#         return "fizz buzz"
#     elif x % 3 == 0:
#         return "fizz"
#     elif x % 5 == 0:
#         return "buzz"
#     else:
#         return x


# input("Play Fizz Buzz. Press ENTER to start")
# print()


# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_answer = fizz_buzz(next_number)
#     # players_answer = int(input("Your go: "))
#     players_answer = correct_answer
#     if players_answer != correct_answer:
#         print("You lose, the correct answer was {}".format(correct_answer))
#         break
# else:
#     print("Well done, you reached {}".format(next_number))


def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1
 
    result = 2
    for x in range(3, n + 1):
        result *= x
 
    return result
 
 
for i in range(36):
    print(i, factorial(i))










