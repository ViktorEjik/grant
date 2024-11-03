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
        # self.url = "http://81.90.180.2/api.php"
        self.config = dotenv_values(dotenvPath)
        print(self.config)
