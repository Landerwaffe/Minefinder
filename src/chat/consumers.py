import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import datetime
 
 
class ChatConsumer(WebsocketConsumer):
    # websocket connect
    def connect(self):
        # get chat room from url, and set up a channel
        # print(self.scope)
        self.user_name = self.scope['session'].get('user_name', None)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # add channels
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        # accept all request
        self.accept()

    # websocket disconnect
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # 从websocket receive
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # set message to the channel
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user_name,
                'message': message
            }
        )

    # post message
    def chat_message(self, event):
        message = event['message']
        user = event['user']
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # set message to the user
        self.send(text_data=json.dumps({
            'message': f'''User:{user} Time:{datetime_str}:\n{message}'''
        }))
