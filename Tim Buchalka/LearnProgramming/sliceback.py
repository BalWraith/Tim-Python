import os;os.system('cls')
#          01234567891234567891234567
letters = "abcdefghijklmnopqrstuvwxyz"
#                  start:stop:step
backwards = letters[25:0:-1]  # 'zyxwvutsrqponmlkjihgfedcb' missing 'a'
backwardAll = letters[::-1]    # 'zyxwvutsrqponmlkjihgfedcba' includes 'a'
qpo = letters[-10:-13:-1] # 'qpo'
edcba = letters[-22:-27:-1] # 'edcba' 

print(backwards)
print(backwardAll)
print(qpo)
print(edcba)
print(letters[:1]) # 'a'
computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]