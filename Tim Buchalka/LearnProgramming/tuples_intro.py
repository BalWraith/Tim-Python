albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ];import os;os.system('cls')

# print(len(albums))
#this is more effecint 
for name, artist,year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist,year))
    
# for albums in albums:
#     name, artist, year = albums
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(name, artist,year))









