from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path(r'ws/socket-server/rooms/<str:pk>/', consumers.RoomConsumer.as_asgi())
]