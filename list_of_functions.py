import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import time
import os
import json
import datetime
from dotenv import load_dotenv
from datetime import datetime
import time

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

# 1. Current Track INFO
def current_track():
    global prev_data
    nowplaying = sp.current_playback()

    if nowplaying is not None and nowplaying['is_playing']:
        name = nowplaying['item']['name']
        artist = nowplaying['item']['artists'][0]['name']
        album = nowplaying['item']['album']['name']
        statement = f"\n\nNow Playing on Spotify: \n\nName: {name}\nArtist: {artist}\nAlbum: {album}"

        if statement != prev_data:
            print(statement)
            print(f"Playing on {nowplaying['device']['name']}")
            prev_data = statement
    else:
        print("No track is playing right now.")


#2. Top Tracks of an Artist
def top_ten_songs_of_artist():
    input_artist_name = input("Name of the artist. ")
    results = sp.search(q='artist:' + input_artist_name, type='artist')

    artist_name = results['artists']['items'][0]['name']
    artist_id = results["artists"]['items'][0]['id']
    top_tracks = sp.artist_top_tracks(artist_id)
    print(f"\nHere are the top ten tracks of {artist_name}\n")

    i = 1
    for x in top_tracks['tracks']:
        print(f"{i}. {x['name']}.")
        i += 1


# 3. Artists followed by the user on Spotify
def followed_artists():
    artists = sp.current_user_followed_artists()

    i = 1
    print("List of artists:")
    for x in artists['artists']['items']:
        print(f"{i}. {x['name']}")
        i += 1

# 4. Get Top Songs by Artist Name
def top_artists(st_duration):
    i = 1

    top_artists = sp.current_user_top_artists(limit=30, offset=0, time_range=st_duration)
    print("Here are your top 30 artists.\n")

    for x in top_artists['items']:
        print(f"{i}. {x['name']}")
        i += 1


# 5
def devices():
    devices = sp.devices()


    print("Active Devices:\n")
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

#8
def add_to_queue(track_name):
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
        sp.add_to_queue(uri=track_uri)
        print(f"\nAdded to Queue: {name} - {artist}\nAlbum: {album}\nRelease Date: {release_date}\nPopularity: {popul}")
    else:
        print(f"Track not found: {track_name}. Try again")

# 9
def top_songs(st_duration):
    i = 1
    top_songs = sp.current_user_top_tracks(limit=20, offset=0, time_range=st_duration)
    print("Here are your top 20 songs.\n")
    for x in top_songs['items']:
        print(f"{i}. {x['name']}")
        i += 1

#10
def queue():
    data = sp.queue()

    name = data['currently_playing']['name']
    link = data['currently_playing']['href']

    queue = data['queue']
    i=1
    print("Queue\n")
    for item in queue[:10]:

        qname = item['name']
        qlink = item['href']
        qartist = item['artists'][0]['name']
        qalink = item['artists'][0]['href']

        print(f'{i}. {qname} - {qartist}')
        i+=1

#11
def next():
    sp.next_track()
    time.sleep(2)
    nowplaying = sp.current_playback()

    if nowplaying is not None and nowplaying['is_playing']:
        name = nowplaying['item']['name']
        artist = nowplaying['item']['artists'][0]['name']
        album = nowplaying['item']['album']['name']
        statement = f"\n\nNow Playing on Spotify: \n\nName: {name}\nArtist: {artist}\nAlbum: {album}"

        print(statement)

#12
def previous():
    sp.previous_track()
    time.sleep(2)
    nowplaying = sp.current_playback()

    if nowplaying is not None and nowplaying['is_playing']:
        name = nowplaying['item']['name']
        artist = nowplaying['item']['artists'][0]['name']
        album = nowplaying['item']['album']['name']
        statement = f"\n\nNow Playing on Spotify: \n\nName: {name}\nArtist: {artist}\nAlbum: {album}"

        print(statement)