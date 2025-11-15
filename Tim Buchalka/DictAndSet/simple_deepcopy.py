from contents import recipes
import os;os.system('cls')

def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.
    
    #!The function will crash with an AttributeError if the value aren't lists or dictionaries.
    
    :param d: The dictionary to copy.
    :return: A copy of the `d`, with the values being copies of the original value.
    """

    new_dict = {}
    for key,value in d.items():
        new_value = value.copy()#*Shallow copy of the value
        new_dict[key] = new_value#*Assign the copied value to the new dictionary

    return new_dict #*Return the new dictionary





recipes_copy = my_deepcopy(recipes)    
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
    
