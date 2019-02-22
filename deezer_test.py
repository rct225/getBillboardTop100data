
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import urllib
import json



CLIENT_ID = "330182"
CLIENT_SECRET = "00c65d6930b4b991ef880aead3af5220"

REDIRECT_URI = "https://tc080y38.apps.lair.io/callback"
AUTHORIZE_URL = "https://connect.deezer.com/oauth/auth.php"
ACCESS_TOKEN_URL = "https://connect.deezer.com/oauth/access_token.php"


def search_deezer(artist, track, token):

    # query = "https://rct225.pythonanywhere.com/test?artist=" + artist + "&track=" + track
    query = "https://api.deezer.com/search?q=artist:\"" + artist + "\"%20track:\"" + track + "\"" + "&access_key=" + token

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    # print(query)
    results = requests.get(query, headers=headers).content

    return results.decode('utf-8')


# deezer = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
# authorization_url, state = deezer.authorization_url(AUTHORIZE_URL)
#
# d2 = OAuth2Session(CLIENT_ID, state=state)
# token = d2.fetch_token(ACCESS_TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=REDIRECT_URI)
#
# print(token)

token = "frMuTEC5FiFQ9uSImyjXhr7CL2MNvPL65y9hWWQ95OjhL1AnGj"

test = search_deezer("Ramones", "Rockaway Beach", token)

data = json.loads(test)
print(data['data'][0]['id'])
#
# res = oauth.put("https://api.deezer.com/user/me?access_token=" + token["access_token"])
# print(res)


