from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'conversations', 'messages_sent')


class ConversationSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())

    class Meta:
        model = Conversation
        fields = ('id', 'participants', 'messages', 'created_at')


class MessageSerializer(serializers.ModelSerializer):
    conversations = serializers.PrimaryKeyRelatedField(many=True, queryset=Conversation.objects.all())

    class Meta:
        model = Message
        fields = '__all__'

    # def create(self, validated_data):
    #     conversation_data = validated_data.pop('conversations')
    #     message = Message.objects.create(**validated_data)
    #     Conversation.objects.create(message=message, **conversation_data)
    #     return message
