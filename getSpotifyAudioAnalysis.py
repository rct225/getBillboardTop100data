import csv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id="ff5998c858ec4e148874d174d4ece89d", client_secret="33f1bdf6e3aa4397bc655601c92582bf")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

fh = open('test_spotify_audio_analysis.txt', 'w+')
fhe = open('test_spotify_audio_analysis_error.txt', 'w+')

columns = ["Track","Artist","DeezerId","isrc","SpotifyId"]

# print("Track,Artist,DeezerId,isrc,SpotifyId", file=fh)
# headers = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
# header = ",".join(columns) + "," + ",".join(headers)

# print(header,file=fh)
with open('test_spotifyId.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        res = sp.audio_analysis(row["SpotifyId"])
        print(res.keys())