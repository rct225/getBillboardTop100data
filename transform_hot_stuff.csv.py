import csv
import collections
import itertools
import functools

unique_songs = collections.defaultdict(functools.partial(next, itertools.count()))

columns = ["url", "WeekID", "Week Position",
           "Song", "Performer", "SongID",
           "Instance", "Previous Week Position",
           "Peak Position", "Weeks on Chart",
           "uniqueSongId"]

fh = open('billboard_hot_100_1958_2018.tsv', 'w+')

print("\t".join(columns), file=fh)

with open('Hot Stuff.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        uniqueSongId = unique_songs[row["Song"]]
        row_data = "\t".join([v for k, v in row.items()]) + "\t" + str(uniqueSongId)
        print(row_data, file=fh)

fh.close()


