import requests

USERNAME = "Admin@my_bot"
PASSWORD = "j6ievtgf8to4olgv6r3dcpu0ngc9hnke"

S = requests.Session()

URL = "http://81.90.180.2/w/api.php"

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
print(S.get(url=URL, params=PARAMS_0))
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

PARAMS_1 = {
    'action': "login",
    'lgname': USERNAME,
    'lgpassword': PASSWORD,
    'lgtoken': LOGIN_TOKEN,
    'format': "json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
assert DATA['login']['result'] == 'Success'