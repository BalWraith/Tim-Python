import os;os.system('cls')
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
cap = []
for char in quote:
    if char == char.upper():
        cap.append(char)
print(cap)        