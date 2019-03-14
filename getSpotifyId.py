import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id="ff5998c858ec4e148874d174d4ece89d",
                                                      client_secret="33f1bdf6e3aa4397bc655601c92582bf")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

fh = open('test_spotifyId.txt', 'w+')
fhe = open('test_spotifyId_error.txt', 'w+')


print("title\tartist\tuniqueSongId\tdeezerId\tisrc\tspotifyId", file=fh)
print("title\tartist\tuniqueSongId\tdeezerId\tisrc\tspotifyId", file=fhe)

with open('test_isrc.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        isrc = row["isrc"]
        print(isrc)
        data = "\t".join([v for k, v in row.items()])
        try:
            result = sp.search(q="isrc: "+isrc, limit=20, offset=0, type='track')
            if len(result["tracks"]["items"]) > 0:

                print(data + "\t" + result["tracks"]["items"][0]["id"], file=fh)
            else:
                print(data + "\t" + "NOT_FOUND", file=fhe)
        except:
            print(data + "\t" + "ERROR", file=fhe)
            continue

fh.close()
fhe.close()
