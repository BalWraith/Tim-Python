import copy,os;os.system('cls') # deep copy

animals = {
        "lion": ["scary","big","cat"],
        "elephant": ["big","grey","wrinkled"],
        "teddy": ["cuddly","stuff"],
}

# Perform a shallow copy
# things = animals.copy()#* things is the new copy of the animals dict

# Perform a deep copy
things = copy.deepcopy(animals)

print(id(things["teddy"]),things["teddy"])#* id(things) 
print(id(animals["teddy"]),animals["teddy"])#* id(animals)

print()

things["teddy"].append("toy")
print(things["teddy"])#* cuddly, stuff, toy
print(animals["teddy"])#*cuddly, stuff, toy







""" NOTE
Deep copy     : `deepcopy()` recursively inserts copies of the objects found in the original

 Shallow copy : `copy()` populates the new compound object with references to the objects found in the oringinal"""