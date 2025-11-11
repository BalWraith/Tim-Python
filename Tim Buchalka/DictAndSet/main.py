import os;os.system('cls')

dog_dict = {
    'Claire': 'German Shepherd', 
    'Maddy':  'Blue Heeler',
    'Neicha': 'Bernese Mountain Dog / Poodle',
    'Ace':    'Pitbull / Terrier',
    'Nina':   'English Mastiff',
    'Kira':   'Retriever'
}
dog_dict = sorted(dog_dict)
for key in dog_dict:
    print(key)
    