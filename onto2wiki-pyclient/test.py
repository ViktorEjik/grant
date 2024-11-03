import requests

USERNAME = "Admin@my_bot"
PASSWORD = "tdnpuln46kpq3kuuvoumetl50vtr3kdg"
PASSWORD = "tdnpuln46kpq3kuuvoumetl50vtr3kg"
S = requests.Session()

URL = "http://81.90.180.2/api.php"

# Retrieve login token first
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}
heads ={
    'User-Agent': 'PostmanRuntime/7.42.0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Cookie': 'my_wiki_session=rl0o3dtr7sghonrfku5dpmjbq07i1fco',
}

R = S.get(url=URL, params=PARAMS_0, headers=heads)
print(R.request.url, R.status_code, R.text, R.request.headers)
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

R = S.post(URL, data=PARAMS_1, headers=heads)
DATA = R.json()

print(DATA)
assert DATA['login']['result'] == 'Success'