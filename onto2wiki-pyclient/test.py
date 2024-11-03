import Onto2WikiClient

# USERNAME = "Admin@my_bot"
# PASSWORD = "uqg8slmblghmuktop21cl5sqs2flf8fo"
#
# S = requests.Session()
#
# URL = "http://81.90.180.2/api.php"
#
# # Retrieve login token first
# PARAMS_0 = {
#     'action':"query",
#     'meta':"tokens",
#     "type": "login|csrf",
#     'format':"json"
# }
# heads ={
#     'User-Agent': 'myapp',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept': '*/*',
#     'Connection': 'keep-alive',
# }
#
# R = S.get(url=URL, params=PARAMS_0, headers=heads)
# print(R.request.url, R.status_code, R.text, R.request.headers)
# DATA = R.json()
#
# LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
# CSRF = DATA['query']['tokens']['csrftoken']
#
# print(LOGIN_TOKEN)
# print(CSRF)
#
# # Send a post request to login. Using the main account for login is not
# # supported. Obtain credentials via Special:BotPasswords
# # (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
#
# PARAMS_1 = {
#     'action': "login",
#     'lgname': USERNAME,
#     'lgpassword': PASSWORD,
#     'lgtoken': LOGIN_TOKEN,
#     'format': "json"
# }
#
# R = S.post(URL, data=PARAMS_1, headers=heads)
# DATA = R.json()
#
# print(DATA)
# assert DATA['login']['result'] == 'Success'
#
# PARAMS_0 = {
#     'action':"query",
#     'meta':"tokens",
#     "type": "csrf",
#     'format':"json"
# }
#
# R = S.get(url=URL, params=PARAMS_0, headers=heads)
#
# DATA = R.json()
#
# # LOGIN_TOKEN = DATA['query']['tokens']['logintoken']
# CSRF = DATA['query']['tokens']['csrftoken']
#
# print(LOGIN_TOKEN)
# print(CSRF)
#
# PARAMS_2 = {
#     'action': "loguot",
#     'lgtoken': CSRF,
#     'format': "json"
# }
# R = S.post(URL, data=PARAMS_2, headers=heads)
# print(R.request.url, R.status_code, R.text, R.request.headers, sep='\n')
testSess = Onto2WikiClient.Onto2WikiClient()
testSess.login()
testSess.daa_new_page({"title": "Test", "text": "Test"})