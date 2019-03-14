import csv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id="ff5998c858ec4e148874d174d4ece89d",
                                                      client_secret="33f1bdf6e3aa4397bc655601c92582bf")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

fh = open('test_spotify_audio_features.txt', 'w+')
fhe = open('test_spotify_audio_features_error.txt', 'w+')

columns = ["title", "artist", "uniqueSongId", "deezerId", "isrc", "spotifyId"]

headers = ['danceability', 'energy', 'key', 'loudness', 'mode',
           'speechiness', 'acousticness', 'instrumentalness',
           'liveness', 'valence', 'tempo', 'uri', 'track_href',
           'analysis_url', 'duration_ms', 'time_signature']

header = "\t".join(columns) + "\t" + "\t".join(headers)
error_header = "\t".join(columns) + "\t" + "error"
print(header, file=fh)
print(error_header, file=fhe)

with open('test_spotifyId.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        print(row["title"])
        row_data = "\t".join([v for k, v in row.items()])
        try:
            res = sp.audio_features([row["spotifyId"]])[0]
            data = []
            for h in headers:
                data.append(str(res[h]))
                # print(h + " " + str(res[h]))

            # print(row_data)
            row_entry = "\t".join(data)
            # print(row_entry)
            new_row = row_data + "\t" + row_entry
            print(new_row, file=fh)
        except:
            print(row_data + "\t" + "ERROR")

fh.close()
fhe.close()
