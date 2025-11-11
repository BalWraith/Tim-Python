a = b = c = d = e = f = 12;import os;os.system('cls')
print(c)

x,y,z = 1,2,76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1,2,76 # data represents a tuple
x,y,z = data # ^^^^^^^^^^^^^^ unpacking
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
data_list.append(15)# this will crash the code at line 22 because all values are not being assigned to variables

p,q,r = data_list
print(p)
print(q)
print(r)















