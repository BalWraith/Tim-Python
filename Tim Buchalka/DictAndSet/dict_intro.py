import os;os.system('cls')
#? (key: value) pair
vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawaski ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': "Yamaha XT650",
    'jimny': 'Suzuki Jimmy 1.5',
    'fiesta': "Ford Fiesta Ghia 1.4",
    'learjet': 'Bombardier Learjet 75'
    
}
#* indexing (key: value,) Faster
#!ERROR key not found it will cause an error
my_car = vehicles['fiesta']

commuter = vehicles['virago']

#* get method (key: value,) Slower
#!ERROR wiil return (None) and will not error 
learner = vehicles.get("er5")

#? How to add to a (vehicles["key"] = "value") pair
vehicles["starfighter"] = "Lockheed F-104"
vehicles["leerjet"] = "Bombardier Learjet 45"
vehicles["toy"] = "glider"



#?This is how to iterate over a (key: value) pair 
#* uses less memory
# for key in vehicles:
#     print(key, vehicles[key],sep=', ')

#* Changing an existing value
vehicles["virago"] = 'Yamaha XV535'

#* Deleting a (key: value,)
del vehicles["starfighter"]

#!Error
# del vehicles["f1"]

#!Error
# vehicles.pop("f1")
#* Nothing will happen

#* Will print None 
# result = vehicles.pop("f1", None)
# print(result)

#* This will print "This will return nothing"
# result = vehicles.pop("f1", "This will return nothing")
# print(result)
# plane = vehicles.pop("learjet")
# print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()


#* .item() uses more memory
# spot = 0
# for key, value in vehicles.items():
#     spot +=1
#     print(spot,key,value,sep=': ')


def apple():
    print("apple")



