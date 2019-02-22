import csv
# import requests
import pprint
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_credentials_manager = SpotifyClientCredentials(client_id="ff5998c858ec4e148874d174d4ece89d", client_secret="33f1bdf6e3aa4397bc655601c92582bf")

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

fh = open('test_clean.txt', 'w+')

# Track,Artist,DeezerId,isrc
with open('isrc-test.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        isrc = row["isrc"]
        print(isrc)
        result = sp.search(q="isrc: "+isrc, limit=20, offset=0, type='track')
        if len(result["tracks"]["items"]) > 0:
            print(result["tracks"]["items"][0]["id"])
        else:
            print("Can't find" + row["Track"])

fh.close()