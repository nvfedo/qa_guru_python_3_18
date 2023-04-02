from dataclasses import dataclass


@dataclass
class Hosts:
    def __init__(self, env):
        self.demoqa = {
            'local': 'localhost:5555',
            'dev': 'http://dev_demowebshop.com',
            'prod': 'https://demowebshop.tricentis.com/',
        }[env]
        self.reqres = {
            'local': 'localhost:5555',
            'dev': 'http://dev_reqres.in/',
            'prod': 'https://reqres.in/',
        }[env]
