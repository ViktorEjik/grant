from os.path import split

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
        req = self.get(url=self.config['URL_API'], params=params, headers=self.headers)
        self.config.update(req.json()['query']['tokens'])
        if "LOGIN" in self.config and "PASSWORD" in self.config:
            log_params = {
                "action": "login",
                'lgname': self.config['LOGIN'],
                'lgpassword': self.config['PASSWORD'],
                'lgtoken': self.config['logintoken'],
                'format': "json"
            }
            req = self.post(self.config['URL_API'], data=log_params, headers=self.headers).json()
            if req['login']['result'].lower() != 'success':
                raise Exception("Login failed: " + req['login']['reason'])
            self.config.update({'lgusername': req['login']['lgusername']})
            req = self.get(url=self.config['URL_API'], params=params, headers=self.headers)
            self.config.update(req.json()['query']['tokens'])
            print(self.config)

    def get_hierarchy_page(self, pages, me, visited, i):
        text = f'{"*" * i} [[{' '.join(me.split('_'))}]]\n'
        visited.append(me)

        for children in pages[me].get('children', ''):
            if children not in visited:
                text += self.get_hierarchy_page(pages, children, visited, i + 1)
        return text

    def add_hierarchy_page(self, page_name: str, pages, roots):
        text = 'lkuj'
        for root in roots:
            me = root
            visited = ['']
            i = 1
            text = self.get_hierarchy_page(pages, me, visited, i)
        params = {
            "action": "edit",
            "format": "json",
            "title": page_name,
            "text": "Данная страница сгенерирована ботом, её необходимо заполнить.<br>" + text,
            "bot": 1,
            "token": self.config['csrftoken'],
            "formatversion": "2"
        }
        req = self.post(url=self.config['URL_API'], data=params, headers=self.headers).json()
        print(req)

    def add_new_page(self, page):
        text = page.get('text', '')
        params = {
            "action": "edit",
            "format": "json",
            "title":  page['title'],
            "text": text + "Данная страница сгенерирована ботом, её необходимо заполнить.",
            "bot": 1,
            "token": self.config['csrftoken'],
            "formatversion": "2"
        }
        req = self.post(url=self.config['URL_API'], data=params, headers=self.headers).json()
        print(req)
        if 'children' in page:
            childrens = ''
            for children in page['children']:
                childrens += '* [[' + ' '.join(children.split("_")) + ']]' + '\n'
            params = {
                "action": "edit",
                "format": "json",
                "title": page['title'],
                "section": "new",
                "sectiontitle": "Childrens",
                "text": childrens,
                "bot": 1,
                "token": self.config['csrftoken'],
                "formatversion": "2"
            }
            req = self.post(url=self.config['URL_API'], data=params, headers=self.headers).json()
            print(req)
        if 'parent' in page:
            params = {
                "action": "edit",
                "format": "json",
                "title": page['title'],
                "section": "new",
                "sectiontitle": "Parent",
                "text": '* [[' + ' '.join(page['parent'].split('_')) + ']]' + '\n',
                "token": self.config['csrftoken'],
                "formatversion": "2"
            }
            req = self.post(url=self.config['URL_API'], data=params, headers=self.headers).json()
            print(req)

    def dell_page(self, page):
        params = {
            "action": "delete",
            "format": "json",
            "title": page['title'],
            "token": self.config['csrftoken'],
            "formatversion": "2"
        }
        req = self.post(url=self.config['URL_API'], data=params, headers=self.headers).json()
        print(req)