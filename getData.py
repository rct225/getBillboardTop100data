import csv
# import requests
import pprint
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

unique_songs = {}
with open('Hot Stuff.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        unique_songs[row["Song"]] = row["Performer"]

print(len(unique_songs.keys()))

#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row["WeekID"]} {row["Week Position"]} {row["Song"]} {row["Performer"]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')


client_credentials_manager = SpotifyClientCredentials(client_id="ff5998c858ec4e148874d174d4ece89d", client_secret="33f1bdf6e3aa4397bc655601c92582bf")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# results = sp.search(q='Zazueira artist:Herb Alpert & The Tijuana Brass', limit=20)
# print(results)
fh = open("test_file.txt", "a")

for song in unique_songs.keys():
    raw_search_string = song
    # print(search_string)
    pattern = re.compile('([^\s\w]|_)+')
    search_string = pattern.sub("", raw_search_string)
    print(search_string)
    results = sp.search(q=search_string, type='track', limit=20)
    # print(results)
    # if results:
    if results["tracks"]["total"] != 0:
        t = results["tracks"]["items"][0]["id"]
        print(song + "," + unique_songs[song] + "," + t,file=fh)
    else:
        print(song + " by " + unique_songs[song] + " not found", file=fh)

fh.close()

#
# t = results["tracks"]["items"][0]["id"]
#
# info = sp.track(t)
#
# print(t)
# pprint.pprint(info)
#
# # start = time.time()
# features = sp._get("audio-features/" + t)
#
# print(features)
