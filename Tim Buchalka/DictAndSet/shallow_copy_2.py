lion_list = ["scary","big","cat"]
elephant_list = ["big","grey","wrinkled"]
teddy_list = ["cuddly","stuff"]

animals = {
        "lion": lion_list,
        "elephant": elephant_list,
        "teddy": teddy_list,
}

# things = animals.copy()#* things is the new copy of the animals dict
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(things["teddy"])#* cuddly, stuff
print(animals["teddy"])#*cuddly, stuff

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(things["teddy"])#* cuddly, stuff, toy
print(animals["teddy"])#*cuddly, stuff, toy
print(teddy_list)






