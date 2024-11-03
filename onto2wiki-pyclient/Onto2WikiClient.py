import requests
from dotenv import dotenv_values


class Onto2WikiClient(requests.Session):
    def __init__(self, dotenvPath='.env'):
        super(Onto2WikiClient, self).__init__()
        self.headers = {
            'User-Agent': 'Onto2WikiClient',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': '*/*',
            'Connection': 'keep-alive',
        }
        self.config = dotenv_values(dotenvPath)

    def login(self):
        params = {
            'action':"query",
            'meta':"tokens",
            "type": "login|csrf",
            'format':"json"
        }
        req = self.get(url=self.config['URL'], params=params, headers=self.headers)
        self.config.update(req.json()['query']['tokens'])
        if "LOGIN" in self.config and "PASSWORD" in self.config:
            log_params = {
                "action": "login",
                'lgname': self.config['LOGIN'],
                'lgpassword': self.config['PASSWORD'],
                'lgtoken': self.config['logintoken'],
                'format': "json"
            }
            req = self.post(self.config['URL'], data=log_params, headers=self.headers).json()
            if req['login']['result'].lower() != 'success':
                raise Exception("Login failed: " + req['login']['reason'])
            self.config.update({'lgusername': req['login']['lgusername']})
            req = self.get(url=self.config['URL'], params=params, headers=self.headers)
            self.config.update(req.json()['query']['tokens'])
            print(self.config)

    def daa_new_page(self, page: dict[str, str]):
        params = {
            "action": "edit",
            "format": "json",
            "title": page['title'],
            "text": page['text'] + "<br>Данная страница сгенерирована ботом, её необходимо заполнить.",
            "bot": 1,
            "token": self.config['csrftoken'],
            "formatversion": "2"
        }
        req = self.post(url=self.config['URL'], data=params, headers=self.headers).json()
        print(req)
