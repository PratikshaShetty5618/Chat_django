# serializers.py
from rest_framework import serializers

from .models import Login,Chats

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


class ChatsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chats
		fields = '__all__'