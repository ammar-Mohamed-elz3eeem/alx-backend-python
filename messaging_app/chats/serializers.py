from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the User object.
    """
    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username', 'conversations',
                  'messages_sent')


class ConversationSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the Conversation object.
    """
    messages = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Message.objects.all())

    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = Conversation
        fields = ('id', 'participants', 'messages', 'created_at')


class MessageSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the Message object.
    """
    conversations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Conversation.objects.all())

    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = Message
        fields = '__all__'
