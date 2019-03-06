import csv
import lyricsgenius
import re
import time
from random import randint
import sys


files = sys.argv[1:]
print(files)

for f in files:
    fh = open('test_genius_lyrics_' + f + '.txt', 'w+')
    fhe = open('test_genius_lyrics_' + f + '_error.txt', 'w+')

    columns = ["Track","Artist","DeezerId","isrc","SpotifyId","GenuisURL","lyric"]

    # print("Track,Artist,DeezerId,isrc,SpotifyId", file=fh)
    # headers = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    # header = ",".join(columns) + "," + ",".join(headers)

    ACCESS_TOKEN = "ONZMZdv2jGPJkK-f0yppCLUiwWhtUe3t6F6ufHc648TMoG2igt5TgBk7qhle6ovA"

    genius = lyricsgenius.Genius(ACCESS_TOKEN);
    genius.verbose = False
    genius.remove_section_headers = True
    genius.skip_non_songs = True

    header = ",".join(columns)
    error_header = ",".join(columns[0:5])

    print(header, file=fh)
    print(error_header, file=fhe)

    with open(f) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', fieldnames=columns[0:5])

        # next(csv_reader)

        for row in csv_reader:
            track = row["Track"]
            search_track = re.sub(r"\s\(.*\)", "", track)
            time.sleep(1)
            song = genius.search_song(search_track, row["Artist"])
            data = ",".join([v for k, v in row.items()])
            print(track)
            if song is None:
                print(data + ",NOT_FOUND", file=fhe)
            elif song.title.upper() != search_track.upper():
                # print(row, file=fhe)
                # print(song.title + " Track:" + search_track)
                print(data + ",ERROR", file=fhe)
            else:
                url = song.url
                # print(url)
                lyric = song.lyrics
                plyric = lyric.replace("\n", " ")
                print(data + "," + url + "," + "\"" + plyric + "\"",file=fh)
                # print(song.lyrics, file=fh)

    fh.close()
    fhe.close()