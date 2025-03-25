import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Room, Message
from .serializers import UserSerializer, MessageSerializer
from bs4 import BeautifulSoup
import html
class RoomConsumer(WebsocketConsumer):
    def connect(self):

        self.user = self.scope["user"]

        if self.user.is_authenticated:
            self.user.connections_count += 1
            self.user.save()

        self.room_id = self.scope["url_route"]["kwargs"]["pk"]
        self.room = Room.objects.get(id=self.room_id)

        self.room_name = f'room_{self.room_id}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.accept()

        self.send_data()

    def disconnect(self, close_code):
        if self.user.is_authenticated:
            self.user.connections_count -= 1
            self.user.save()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'like-message' in text_data_json:
            like_msg = text_data_json['like-message']
            msg = Message.objects.get(pk=like_msg)
            msg.likes.add(self.user)

        if 'unlike-message' in text_data_json:
            like_msg = text_data_json['unlike-message']
            msg = Message.objects.get(pk=like_msg)
            msg.likes.remove(self.user)

        if 'delete-message' in text_data_json:
            delete_msg = text_data_json['delete-message']
            msg = Message.objects.get(pk=delete_msg)
            if self.user == msg.user:
                msg.delete()
                room = Room.objects.get(id=self.room_id)
                user_msg_count = room.message_set.filter(user=self.user).count()
                if user_msg_count == 0:
                    room.participants.remove(self.user)

        if 'message' in text_data_json:
            message = text_data_json['message']
            # message = BeautifulSoup(message,"html.parser").get_text()
            message = html.escape(message)
            print(message)
            self.create_new_message(message)

        self.send_data()

    def send_data(self):
        room_messages, participants = self.get_room_messages_and_participants()
        serialized_msgs = MessageSerializer(room_messages, many=True, context={'user': self.user}).data
        serialized_participants = UserSerializer(participants, many=True).data

        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type': 'room_messages',
                'messages': serialized_msgs,
                'participants': serialized_participants,
            }
        )

    def room_messages(self, event):
        messages = event['messages']
        participants = event['participants']
        self.send(text_data=json.dumps({
            'type': 'room_messages',
            'messages': messages,
            'participants': participants,
        }))

    def get_room_messages_and_participants(self):
        room = Room.objects.get(id=self.room_id)
        participants = room.participants.all()
        return list(room.message_set.all().order_by('-created')), list(participants)

    def create_new_message(self, text_str):
        message = Message.objects.create(
            user=self.user,
            room=self.room,
            body=text_str
        )
        self.room.participants.add(self.user)