numbers = (0,1,2,3,4,5);import os;os.system('cls')

# print(numbers, sep=";")#* tuples count as a single item
# print(*numbers, sep=";")#* the * unpacks the tuple 
# print(0,1,2,3,4,5, sep=";")


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0,1,2,3,4,5)

print()
test_star()



