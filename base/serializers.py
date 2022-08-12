from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.utils.timesince import timesince
from .models import User, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['user_name', 'created', 'body', 'user_id', 'user_avatar_url', 'id', 'likes', 'liked', 'user_online_status_class']

    created = SerializerMethodField('convert_created_to_timesince')
    user_name = SerializerMethodField('get_user_name')
    user_id = SerializerMethodField('get_user_id')
    user_avatar_url = SerializerMethodField('get_user_avatar_url')
    likes = SerializerMethodField('get_likes')
    liked = SerializerMethodField('get_liked')
    user_online_status_class = SerializerMethodField('get_user_online_status_class')

    def convert_created_to_timesince(self, obj):
        return timesince(obj.created)

    def get_user_name(self, obj):
        return obj.user.username

    def get_user_id(self, obj):
        return obj.user.id

    def get_user_avatar_url(self, obj):
        return obj.user.avatar.url

    def get_likes(self, obj):
        return obj.likes.count()

    def get_liked(self, obj):
        user = self.context.get("user")
        if obj.likes.filter(pk=user.pk).exists():
            return True
        else:
            return False

    def get_user_online_status_class(self, obj):
        return obj.user.get_online_status_class()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'avatar_url', 'online_status_class']

    avatar_url = SerializerMethodField('get_avatar_url')
    online_status_class = SerializerMethodField('get_online_status_class')

    def get_avatar_url(self, obj):
        return obj.avatar.url

    def get_online_status_class(self, obj):
        return obj.get_online_status_class()