import os;os.system('cls') #TODO Remove line
available_parts_dict = {"1": "computer",
                        "2": "monitor",
                        "3": "keyboard",
                        "4": "mouse",
                        "5": "hdmi cable",
                        "6": "dvd drive",
                        }
available_parts_list = ["computer",
                        "monitor",
                        "keyboard",
                        "mouse",
                        "hdmi cable",
                        "dvd drive",
                        ]

current_choice = None
part_list = []
while current_choice != "0":
    current_choice = input("> ")
    if current_choice == "0":
        os.system('cls')
        print("Parts Chosen")
        for index,part in enumerate(part_list):
            print(f"{index+1}. {part}")
        break

    elif current_choice in available_parts_dict:
        chosen_part = available_parts_dict[current_choice]
        print(f"Adding {chosen_part}")
        part_list.append(chosen_part)

    else:
        print("Please add options from the list:")
        for i in available_parts_dict:
            print(i,available_parts_dict[i])
        print("0: to finish")     
    






