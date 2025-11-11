"""
`get()` and `setdefault()` methods for dictionaries.
both allows you to provide a default value if the key is not found

`setdefault()` will add the key to the dictionary with the default value if the key is not found

"""


from contents import pantry

chicken_quantity = pantry.setdefault("chicken",0)#* get the value of "chicken"(from the imported mod pantry),if not found, set it to 0
print(f"chicken: {chicken_quantity}")


beans_quantity = pantry.setdefault("beans",0)#* get the value of "beans" (from the imported mod pantry), if not found, set it to 3
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup",0)#* get the value of "ketchup"(from the imported mod pantry),if not found, set it to 5
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini",8)
print(f"zucchini: {z_quantity}")
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)

#* different ways to create the same dictionary
a = dict(one=1, two=2, three=3)
b = { "one":1, "two":2, "three":3}
c = dict(zip(['one','two','three'], [1,2,3]))
d = dict([('two',2), ('one',1), ('three',3)])
e = dict({'three':3, 'one':1, 'two':2})
f = dict({'one': 1, 'three': 3}, two= 2)
# zz = a == b == c == d == e == f #* all are True







