import csv
import lyricsgenius

fh = open('test_genius_lyrics.txt', 'w+')
fhe = open('test_genius_lyrics_error.txt', 'w+')

columns = ["Track","Artist","DeezerId","isrc","SpotifyId","GenuisURL","year","lyric"]

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

with open('test_spotifyId.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        song = genius.search_song(row["Track"], row["Artist"])
        track = row["Track"]
        data = ",".join([v for k, v in row.items()])
        print(track)
        if song is None:
            print(data + ",NOT_FOUND", file=fhe)
        elif song.title != row["Track"]:
            # print(row, file=fhe)
            print(data + ",ERROR", file=fhe)
        else:
            url = song.url
            year = song.year
            lyric = song.lyrics
            plyric = lyric.replace("\n", " ")
            print(data + "," + url + "," + year + "," + "\"" + plyric + "\"",file=fh)
            # print(song.lyrics, file=fh)