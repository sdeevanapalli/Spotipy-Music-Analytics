import list_of_functions as lof

print("\n-----------------------------------------------------------------------------------------")
print("Hello. Please Enter the Serial Number of your Choice.\n\n"
      "1. Current Playback.\n"
      "2. Top 10 Songs of any Artist.\n"
      "3. Artists you Follow on Spotify\n"
      "4. Your Top Artist Plays.\n"
      "5. Your Live Devices.\n"
      "6. Personal Information.\n"
      "7. Play Music (song input)\n"
      "8. Add to Queue (song input)\n"
      "9. Your Top Songs.\n"
      "10. View Queue.\n"
      "11. Play Next Track.\n"
      "12. Play Previous Track\n")

var = int(input())
if var == 1:
    lof.current_track()
elif var == 2:
    lof.top_ten_songs_of_artist()
elif var == 3:
    lof.followed_artists()
elif var == 4:
    duration = int(input("Enter Duration.\n\n1. 1 month\n2. 6 months\n3. 1 year\n"))
    if duration == 1:
        st_duration = 'short_term'
    elif duration == 2:
        st_duration = 'medium_term'
    elif duration == 3:
        st_duration = 'long_term'
    lof.top_artists(st_duration)
elif var == 5:
    lof.devices()
elif var == 6:
    lof.personal()
elif var == 7:
    song = input("Enter the name of the song: ")
    lof.play_music(song)
elif var == 8:
    song = input("Enter the name of the song: ")
    lof.add_to_queue(song)
elif var == 9:
    duration = int(input("Enter Duration.\n\n1. 1 month\n2. 6 months\n3. 1 year\n"))
    if duration == 1:
        st_duration = 'short_term'
    elif duration == 2:
        st_duration = 'medium_term'
    elif duration == 3:
        st_duration = 'long_term'
    lof.top_songs(st_duration)
elif var == 10:
    lof.queue()
elif var == 11:
    lof.next()
elif var == 12:
    lof.previous()
else:
    print("Invalid choice. Please try again.")
