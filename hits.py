hits=[]
while True:
    artist = input("What's the name of the artist?: ")
    song = input("What's the name of the song?: ")
    song_info = {"artist":artist,"song":song}
    hits.append(song_info)
    choice = (input("Would you like to add another song? (y/n): ")).lower()
    if  choice == "n" or choice == "no":
        break
print(f"Your best hits are {hits}")
