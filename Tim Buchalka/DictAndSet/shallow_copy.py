animals = {
        "lion": ["scary","big","cat"],
        "elephant": ["big","grey","wrinkled"],
        "teddy": ["cuddly","stuff"],
}

things = animals.copy()#* things is the new copy of the animals dict

print(things["teddy"])#* cuddly, stuff
print(animals["teddy"])#*cuddly, stuff

print()

things["teddy"].append("toy")
print(things["teddy"])#* cuddly, stuff, toy
print(animals["teddy"])#*cuddly, stuff, toy






