from simple_deepcopy import my_deepcopy
import copy,os;os.system('cls')

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

print(original)
print(copy_1)
print(copy_2)