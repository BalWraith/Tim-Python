data = [4,5,104,105,12,15,110,120,130,130,150,
        160,170,183,185,187,188,191,350,5,360];import os;os.system('cls')

min_valid = 100
max_valid = 200
data.sort()

# TODO process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:# find the first value greater than or equal to 100
        stop = index# stop = to the index greater than or equal to 100
        break
print(stop)
del data[:stop]#stops at the index greater than or equal to 100
print(data)


# TODO process the high values in the list
start = 0
for index in range(len(data)-1, -1, -1):# from the end of the list to the beginning
    if data[index] <= max_valid:# find the first value less than or equal to 200
        start = index + 1# + 1 because index starts at 0
        break

print(start)
del data[start:]#starts at the index less than or equal to 200 + 1
print(data)




