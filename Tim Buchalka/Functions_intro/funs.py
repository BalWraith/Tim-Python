import os;os.system('cls')


def mulitply(x , y):
    result = x * y
    return result

def is_palindrome(string):
    return string[::-1] == string


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum(): #* checks if char is number or letter
            string += char #* adds (char) from the loop to (cleaned_str "")
           
    # return cleaned_str == cleaned_str[::-1]
    return is_palindrome(string)

word = input("Please enter a word to check: ").casefold()
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not palindrome".format(word))

    


