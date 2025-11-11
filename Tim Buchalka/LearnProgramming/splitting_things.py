panagram = """The quick brown
fox jumps\tover 
the lazy dog""";import os;os.system('cls')

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
# print(numbers.split(","))


generated_list = ['9', ' ',
                  '2', '2','3',',',
                  '3', '7','2',',',
                  '0', '3','6',',',
                  '8', '5','4',',',
                  '7', '7','5',',',
                  '8', '0','7']

for i in generated_list:
    print(i, end="")
