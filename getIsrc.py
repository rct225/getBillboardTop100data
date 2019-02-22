import csv
import requests
import json
import time

from json.decoder import JSONDecodeError

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

token = "frMuTEC5FiFQ9uSImyjXhr7CL2MNvPL65y9hWWQ95OjhL1AnGj"


def get_isrc(track_id):
    query = "https://api.deezer.com/track/" + str(track_id) + "&access_key=" + token
    time.sleep(0.125)
    results = requests.get(query, headers=headers).content

    return results.decode('utf-8')


fh = open('test_isrc.txt', 'w+')
fhe = open('test_isrc_errors.txt', 'w+')

#Track,Artist,DeezerId
with open('test_deezerId.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        track_id = row["DeezerId"]
        track = row["Track"]
        artist = row["Artist"]
        query = "https://api.deezer.com/track/" + str(track_id)
        # endpoint = "https://api.deezer.com/search?q="


        results = requests.get(query, headers=headers).content

        data = results.decode('utf-8')
        test = json.loads(data)
        # print(test)
        # print(track + "," + artist)
        if "id" in test.keys():
            isrc = test["isrc"]
            deezer_title = test["title"]
            print(track + "," + artist + "," + str(track_id) + "," + isrc, file=fh)
        else:
            print(str(track_id) + "," + data, file=fhe)
        # print(res)
        # if res:
        #     p = res[0]
        #     print(p["title"] + "," + p["artist"]["name"] + "," + str(p["id"]), file=fh)
        # else:
        #     print(song + "," + artist + "," + "EMPTY", file=fhe)

fhe.close()
fh.close()
