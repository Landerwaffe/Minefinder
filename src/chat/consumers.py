import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime


class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
        # Get the chat room name from the url and create a channel group for each room
        # print(self.scope)
        self.user_name = self.scope['session'].get('user_name', None)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Add current channel to channel group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # Accept all websocket requests
        self.accept()

    # Execute method when websocket is disconnected
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Execute function when a message is received from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send a message to the channel group, the channel group calls the chat_message method
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user_name,
                'message': message
            }
        )

    # Execute method after receiving message from channel group
    def chat_message(self, event):
        message = event['message']
        user = event['user']
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Send message to client via websocket
        self.send(text_data=json.dumps({
            'message': f'''User:{user} Time:{datetime_str}:\n{message}'''
        }))
