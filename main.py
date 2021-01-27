import request
import time
import json
import os

# Inicializando a conexão com API
class TelegramBot(self):
    def __init__(self):
        token = '1617152764:AAEfEZThYahcfARvQDSy7em-WlQr8gFfmNg'
        self.url_base = f'https://api.telegram.org/bot{token}/'

# Obtendo novas mensagens
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem ['update_id']
                    chat_id = mensagem['message']['from']['id']
                    primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem, primeira_mensagem)
                    self.responder(resposta,chat_id)

# Obtendo mensagens
    def obter_mensagens(self ,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)