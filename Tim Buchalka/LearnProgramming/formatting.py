import os; os.system('cls') # use 'cls' on Windows, 'clear' on Linux/Mac
# print("0:2 1:4 2:4")
# for i in range(1, 10):
#     print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))# right aligned within 2, 4, 4 spaces respectively
# print()

# print("0:2 1:3 2:4")
# for i in range(1, 10):
#     print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))# right aligned within 2, 4, 4 spaces respectively
    
# print()
    
# print("0:2 1:<3 2:<4")
    
# for i in range(1,10):    
#     print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))# default is right aligned

print("Pi is approximately {0:12}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:12f}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:12.50f}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:52.50f}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:62.50f}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:72.50f}".format(22/7))# right aligned within 12 spaces
print("Pi is approximately {0:<72.54f}".format(22/7))# right aligned within 12 spaces

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))# default is right aligned


    