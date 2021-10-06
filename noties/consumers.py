import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    # groups = ["broadcast"]

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = 'notification_to_'+str(self.room_name)

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # print(self.channel_name, self.room_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        await self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        await self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        await self.close()
        # Or add a custom WebSocket error code!
        await self.close(code=4123)

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass

    async def send_notification(self, event):
        message = event['message']
        post_id = event['post_id']

        # send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'post_id': post_id
        }))
