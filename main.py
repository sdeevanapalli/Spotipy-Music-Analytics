import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import os
import json
import datetime
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
redirect_uri = 'http://localhost:8888/callback'

# Set up Spotipy with OAuth authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=redirect_uri,
                                               scope='user-library-read user-library-modify user-read-private '
                                                     'user-read-email user-read-playback-state '
                                                     'user-modify-playback-state user-read-currently-playing '
                                                     'playlist-read-private playlist-read-collaborative '
                                                     'playlist-modify-public playlist-modify-private user-follow-read '
                                                     'user-follow-modify app-remote-control streaming '
                                                     'user-read-recently-played '
                                                     'user-top-read'))

prev_data: None = None


# 1
def current_track():
    global prev_data
    nowplaying = sp.current_playback()

    if nowplaying is not None and nowplaying['is_playing']:
        name = nowplaying['item']['name']
        artist = nowplaying['item']['artists'][0]['name']
        album = nowplaying['item']['album']['name']
        statement = f"\n\nNow Playing: Name: {name}\nArtist: {artist}\nAlbum: {album}"

        if statement != prev_data:
            print(statement)
            print(f"Playing on {nowplaying['device']['name']}")
            prev_data = statement
    else:
        print("No track is playing right now.")


# 2
def top_ten_songs_of_artist():
    artist_name = input("Name of the artist. ")
    results = sp.search(q='artist:' + artist_name, type='artist')

    artist_id = results["artists"]['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)
    print(f"\nHere are the top ten artists of {artist_name}")

    i = 1
    for x in top_tracks['tracks']:
        print(f"{i}. {x['name']}.")
        i += 1


# 3
def followed_artists():
    artists = sp.current_user_followed_artists()
    # final = json.dumps(artists, indent=4)

    i = 1
    print("List of artists:")
    for x in artists['artists']['items']:
        print(f"{i}. {x['name']}")
        i += 1


# 4

def top_artists():
    i = 1
    top_artists = sp.current_user_top_artists(limit=30, offset=0, time_range='long_term')

    for x in top_artists['items']:
        print(f"{i}. {x['name']}")
        i += 1


# 5
def devices():
    devices = sp.devices()
    final = json.dumps(devices, indent=4)

    for x in devices['devices']:
        print(x['name'])


# 6
def personal():
    intro = sp.me()
    final = json.dumps(intro, indent=4)
    # print(final)

    name = intro['display_name']
    id = intro['id']
    country = intro['country']
    product = intro['product']
    email = intro['email']

    print(f"\nName: {name}\nID: {id}\nCountry: {country}\nUser: {product}\nEmail: {email}")


# 7
def play_music(track_name):
    # Search for the track
    results = sp.search(q=track_name, type='track', limit=1)

    # Check if a track is found
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        name = results['tracks']['items'][0]['name']
        artist = results['tracks']['items'][0]['artists'][0]['name']
        album = results['tracks']['items'][0]['album']['name']
        release_date = results['tracks']['items'][0]['album']['release_date']
        popul = results['tracks']['items'][0]['popularity']

        # Start playback
        sp.start_playback(uris=[track_uri])
        print(f"\nNow Playing: {name} - {artist}\nAlbum: {album}\nRelease Date: {release_date}\nPopularity: {popul}")
    else:
        print(f"Track not found: {track_name}. Try again")


# 8
def top_songs():
    i = 1
    top_songs = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

    for x in top_songs['items']:
        print(f"{i}. {x['name']}")
        i += 1


print("\n-----------------------------------------------------------------------------------------")
print("Hello. Please Enter the Serial Number of your Choice.\n\n"
      "1. Current Playback.\n"
      "2. Top 10 Songs of any Artist.\n"
      "3. Artists you Follow on Spotify\n"
      "4. Your Top Artist Plays.\n"
      "5. Your Live Devices.\n"
      "6. Personal Information.\n"
      "7. Play Music (song input)\n"
      "8. Your Top Songs.\n")

var = int(input())
if var == 1:
    current_track()
elif var == 2:
    top_ten_songs_of_artist()
elif var == 3:
    followed_artists()
elif var == 4:
    top_artists()
elif var == 5:
    devices()
elif var == 6:
    personal()
elif var == 7:
    song = input("Enter the name of the song: ")
    play_music(song)
elif var == 8:
    top_songs()
else:
    print("Invalid choice. Please try again.")

print("End of Code.")

# while True:
#     current_track()
#     time.sleep(1)
