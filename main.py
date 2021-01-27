import request
import time
import json
import os

# Inicializando a conexão com API
class TelegramBot(self):
    def __init__(self):
        token = '1617152764:AAEfEZThYahcfARvQDSy7em-WlQr8gFfmNg'
        self.url_base = f'https://api.telegram.org/bot{token}/'