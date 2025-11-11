from nested_data import albums;import os;os.system('cls')

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums): # from the nested_data index [0][1][2][3]
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break
        
    print("Please choose your song (0 to go back): ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    elif song_choice == 0:
        continue

    print("Playing {}".format(title))
    print("=" * 40)
    break

    










