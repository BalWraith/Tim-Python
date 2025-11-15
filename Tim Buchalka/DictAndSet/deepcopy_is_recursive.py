from simple_deepcopy import my_deepcopy
import copy,os;os.system('cls')

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}
#NOTE#*Both have the same ID
copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Manager")
print(jp_list)

print("Original",original,"\n")
print("deepcopy",copy_1,"\n")
print("My_deepcopy",copy_2)
