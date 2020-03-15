import json
import os

# singleton class for loading config stuff
class AppSettings:
    _instance = None

    def __init__(self): 
        with open('config.json', 'r', encoding='utf-8') as doc:
            self.config = json.load(doc)
        self.config['DISCORD_TOKEN'] = os.getenv('DISCORD_TOKEN')
        self.config['RIOT_API_KEY'] = os.getenv('RIOT_API_KEY')

    def __getitem__(self, name):
        return self.config[name]
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppSettings, cls).__new__(cls)
        return cls._instance
