import requests
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


    def criar_resposta(self, mensagem, primeira_mensagem):
        mensagem = mensagem['message']['text']
        
        if primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f''' Olá bem vindo a nossa Host. Qual dos nossos serviços gostaria de contratar:
1 - VPN{os.linesep}2 - SERVIDORES WEB{os.linesep}3 - CLOUD AZURE{os.linesep} '''

        if mensagem == '1':
            return f'''VPN - R$ 250,00{os.linesep}Confirmar serviço(s/n)'''
        elif mensagem == '2':
            return f'''SERVIDORES WEB - R$ 150,00{os.linesep}Confirmar serviço(s/n)'''
        elif mensagem == '3':
            return f'''CLOUD AZURE - R$ 350,00{os.linesep}Confirmar serviço(s/n)'''

        if mensagem.lower() in ('s', 'sim'):
            return 'Serviço Confirmado'
        elif mensagem.lower() in ('n', 'não'):
            return ''' Serviço não Confirmado! '''
        else:
            return 'Gostaria de acessar o menu de serviços? Digite "menu"'

    def responder(self, resposta, chat_id):
        link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)


# Respondendo as mensagens
def responder(self, resposta, chat_id):
        link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)

