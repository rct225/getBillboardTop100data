import csv
import requests
import json
import time

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3)" +
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

token = "frMuTEC5FiFQ9uSImyjXhr7CL2MNvPL65y9hWWQ95OjhL1AnGj"


fh = open('test_isrc.txt', 'w+')
fhe = open('test_isrc_errors.txt', 'w+')


print("title\tartist\tuniqueSongId\tdeezerId\tisrc", file=fh)
print("title\tartist\tuniqueSongId\tdeezerId\tisrc", file=fhe)

with open('test_deezerId.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_reader:
        track_id = row["deezerId"]
        unique_id = row["uniqueSongId"]
        track = row["title"]
        artist = row["artist"]
        query = "https://api.deezer.com/track/" + str(track_id)

        time.sleep(0.125)
        try:
            results = requests.get(query, headers=headers).content

            data = results.decode('utf-8')
            test = json.loads(data)
            print(track + "," + artist)
            if "id" in test.keys():
                isrc = test["isrc"]
                deezer_title = test["title"]
                print(track + "\t" + artist + "\t" + str(unique_id) + "\t" + str(track_id) + "\t" + isrc, file=fh)
            else:
                print(track + "\t" + artist + "\t" + str(unique_id) + "\t" + str(track_id) + "\t" + "NOT_FOUND",
                      file=fhe)
        except KeyError:
            print(track + "\t" + artist + "\t" + str(unique_id) + "\t" + str(track_id) + "\t" + "ERROR", file=fhe)
            continue


fhe.close()
fh.close()
