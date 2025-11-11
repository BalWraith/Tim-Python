pangram = "The quick brown fox jumps over the lazy dog";import os;os.system('cls')

letters = sorted(pangram) # Sorted in alphabetical order
print(letters)

numbers = [2.3, 4.5, 8.7, 3., 9.2, 1.6]
sorted_numbers = sorted(numbers) # Sorted in ascending order
# print(sorted_numbers) # [1.6, 2.3, 3.0, 4.5, 8.7, 9.2]
# print(numbers)

numbers.sort() # Sort the list in place in ascending order
print(numbers) # [1.6, 2.3, 3.0, 4.5, 8.7, 9.2]

missing_letters = sorted("The quick brown fox jumps over the lazy dog",
                         key=str.casefold) # Sort ignoring case
print(missing_letters)

names = ["Graham", 
         "John", 
         "terry", 
         "eric",
         "Terry", 
         "michael"
    ]
names.sort(key=str.casefold)# key makes the sort case insensitive
print(names)







