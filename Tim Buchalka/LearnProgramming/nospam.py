menu = [
    ["egg", "bacon"],
    ["egg","sausage", "bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","egg","spam","bacon","spam","tomato", "spam"],
    ["spam","egg","spam","spam","bacon","spam"],
];import os;os.system('cls')

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    # print(meal)
    print(", ".join(meal))





