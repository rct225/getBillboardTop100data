import csv
import sqlite3

sqlite3.PARSE_COLNAMES


def date_extract(parse_line):
    return parse_line.split("/")[-1]


conn = sqlite3.connect("musicdata.db")
c = conn.cursor()

header = ['unique_song_id', 'artist', 'title', 'key', 'danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'lyric', 'max_weeks', 'weeks_at_peek', 'weeks_at_peak', 'peak_position', 'negative_sentiments', 'positive_sentiments', 'neutral_sentiments', 'stemmed_words', 'year']


fh = open('master_list_with_year.tsv', 'w+')
print("\t".join(header), file=fh)

with open('song_master_list.tsv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        song_id = row['unique_song_id']
        print(song_id)
        c.execute('SELECT * FROM billboard_hot_100 WHERE unique_song_id=?', (song_id,))
        dd = c.fetchall()
        # print(dd)
        b_data = [(date_extract(d[0]), d[8]) for d in dd]
        print(b_data)
        s_data = sorted(b_data, key=lambda x: x[1])
        print(s_data[0])
        year = s_data[0][0].split("-")[0]
        print(year)
        row_data = [v for k, v in row.items()]
        row_data.append(year)
        o_data = "\t".join([v for v in row_data])
        print(o_data, file=fh)

conn.close()
fh.close()