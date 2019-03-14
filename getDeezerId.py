import csv
import requests
import json
import time

from json.decoder import JSONDecodeError

headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

token = "frMuTEC5FiFQ9uSImyjXhr7CL2MNvPL65y9hWWQ95OjhL1AnGj"


# def search_deezer(artist, track):
#
#     query = "https://api.deezer.com/search?q=artist:\"" + artist + "\"%20title:\"" + track + "\"" + "&access_key=" + token
#
#     results = requests.get(query, headers=headers).content
#
#     return results.decode('utf-8')
#
#
# def get_isrc(track_id):
#
#     query = "https://api.deezer.com/track/" + str(track_id) + "&access_key=" + token
#
#     results = requests.get(query, headers=headers).content
#
#     return results.decode('utf-8')


unique_songs = {}
unique_artists = set()
with open('billboard_hot_100_1958_2018.tsv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        unique_songs[row["Song"]] = {"artist": row["Performer"], "uniqueSongId": row["uniqueSongId"]}
        unique_artists.add(row["Performer"])
        
# fsa = open('song_artist.json', 'w+')
# json.dump(unique_songs, fsa)
# fsa.close()

print(len(unique_songs.keys()))
print(len(unique_artists))

i = 0
fh = open('test_deezerId.txt', 'w+')
fhe = open('test_deezerId_errors.txt', 'w+')

print("title\tartist\tuniqueSongId\tdeezerId", file=fh)
print("title\tartist\tuniqueSongId\tdeezerId", file=fhe)

for song,value in unique_songs.items():
    artist = value["artist"]
    uniqueSongId = value["uniqueSongId"]

    query = "artist:\"" + artist + "\" track:\"" + song + "\""
    endpoint = "https://api.deezer.com/search?q="

    time.sleep(0.125)
    try:
        results = requests.get(endpoint + query, headers=headers).content

        data = results.decode('utf-8')
        test = json.loads(data)
        print(song + "," + artist)
        res = test["data"]
        if res:
            p = res[0]
            print(p["title"] + "\t" + p["artist"]["name"] + "\t" + str(uniqueSongId) + "\t" + str(p["id"]), file=fh)
        else:
            print(song + "\t" + artist + "\t" + str(uniqueSongId) + "\t" + "NOT_FOUND", file=fhe)
    except KeyError:
        print(song + "\t" + artist + "\t" + str(uniqueSongId) + "\t" + "ERROR", file=fhe)
        continue

fhe.close()
fh.close()
