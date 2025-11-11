d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
import os;os.system('cls')
pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

k = d.keys()
print(k)

d[10] = "ten"
print(v)

#* check for membership
print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v) #* => list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the {key}")


for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the {key}")


# Code for "The dict `update` method" lecture
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }

# d.update(d2)# NOTE * updates the d dictionary with d2 key-value pairs
# for key, value in d.items():
#     print(key, value)

# print()

# d.update(enumerate(pantry_items))#* adds key-value pairs from enumerate object
# for key, value in d.items():
#     print(key, value)






# Cdoe for "The remaining `dict` methods" leacture
#***********************************************************
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# apple = d.keys()
# print(apple)

# for item in d:
#     print(item)





