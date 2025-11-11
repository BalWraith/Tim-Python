available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}     # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")


#! ⬇️⬇️⬇️My code⬇️⬇️⬇️

# import os;os.system('cls') #TODO Remove line
# available_parts_dict = {"1": "computer",
#                         "2": "monitor",
#                         "3": "keyboard",
#                         "4": "mouse",
#                         "5": "hdmi cable",
#                         "6": "dvd drive",
#                         }
# available_parts_list = ["GPU",
#                         "CPU",
#                         "RAM 64gb",
#                         "RAM 32gb",
#                         "SSD 1T",
#                         "Fan",
#                         ]
# #*displays the dict available_parts_dict
# print("Please add options from the list:")
# for index in available_parts_dict:

#     print(index,available_parts_dict[index],sep=": ")
# print("0: to finish")    

# current_choice = None

# part_list = {}

# while current_choice != "0":
#     current_choice = input("> ")
# #*breaks out of the loop & prints the parts chosen
#     if current_choice == "0":
#         os.system('cls')
#         print("Parts Chosen")
#         for key,value in enumerate(part_list):
#             print(f"{key+1}. {value}")
#         break
# #*adds item from list to part_list dict
#     elif current_choice in available_parts_dict:
#         chosen_part = available_parts_dict[current_choice]
#         print(f"Adding {chosen_part}")
#         part_list[chosen_part] = None
# #*option not on list
#     else: 
#         print("Please add options from the list:")
#         for index in available_parts_dict:
#             print(index,available_parts_dict[index])
#         print("0: to finish")
        
    






