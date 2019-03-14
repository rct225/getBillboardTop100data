import csv
import lyricsgenius
import re
import time
import sys

# Make sure to remove header row from first file after split - to avoid issues with header not being skipped

files = sys.argv[1:]
print(files)

for f in files:
    fh = open('test_genius_lyrics_' + f + '.txt', 'w+')
    fhe = open('test_genius_lyrics_' + f + '_error.txt', 'w+')

    columns = ["title", "artist", "uniqueSongId", "deezerId", "isrc", "spotifyId", "GenuisURL", "lyric"]

    ACCESS_TOKEN = "ONZMZdv2jGPJkK-f0yppCLUiwWhtUe3t6F6ufHc648TMoG2igt5TgBk7qhle6ovA"

    genius = lyricsgenius.Genius(ACCESS_TOKEN)
    genius.verbose = False
    genius.remove_section_headers = True
    genius.skip_non_songs = True

    header = "\t".join(columns)
    error_header = "\t".join(columns[0:6])

    print(header, file=fh)
    print(error_header, file=fhe)

    with open(f) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t', fieldnames=columns[0:6])

        # next(csv_reader)

        for row in csv_reader:
            track = row["title"]

            # Regex for removing parentheses - Genius search doesn't seem to like them very much
            search_track = re.sub(r"\s\(.*\)", "", track)
            data = "\t".join([v for k, v in row.items()])
            time.sleep(.33)
            try:
                song = genius.search_song(search_track, row["artist"])

                print(track)
                if song is None:
                    print(data + "\tNOT_FOUND", file=fhe)
                elif song.title.upper() != search_track.upper():
                    # print(row, file=fhe)
                    # print(song.title + " Track:" + search_track)
                    print(data + "\tERROR", file=fhe)
                else:
                    url = song.url
                    # print(url)
                    lyric = song.lyrics
                    plyric = lyric.replace("\n", " ")
                    print(data + "\t" + url + "\t" + plyric, file=fh)
                    # print(song.lyrics, file=fh)
            except TypeError:
                print(data + "\tERROR", file=fhe)
                continue

    fh.close()
    fhe.close()
