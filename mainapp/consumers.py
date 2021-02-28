import json
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            self.send(json.dumps({'message': f"Сообщение номер {i}"}))
            sleep(1)

