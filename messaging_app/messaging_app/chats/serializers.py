from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the User object.
    """
    full_name = serializers.SerializerMethodField()
    role = serializers.CharField(required=True)

    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = User
        fields = ('user_id', 'email', 'first_name', 'last_name',
                  'full_name', 'phone_number', 'role', 'date_joined')

    def get_full_name(self, obj):
        """
        Gets the full name of the user object by
        combining both first & last name.
        """
        return f"{obj.first_name} {obj.last_name}"

    def validate_email(self, value):
        """
        This is a custom validator for the email field
        to retrict some domains from being registered
        for emails on the app.
        """
        restricted_domains = ['example.com', 'gmail.com']
        domain = value.split("@")[-1]
        if domain in restricted_domains:
            raise serializers.ValidationError(f"Emails from \
                {value} are not allowed.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the Conversation object.
    """
    participants_names = serializers.SerializerMethodField()

    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = Conversation
        fields = ('conversation_id', 'participants', 'participants_names',
                  'created_at')

    def get_participants_names(self, obj):
        """
        This is a custom method on this serializer that get all
        participants full names
        """
        return [f"{participant.first_name} {participant.last_name}"
                for participant in obj.participants.all()]


class MessageSerializer(serializers.ModelSerializer):
    """
    This is the json representation for the Message object.
    """
    sender_name = serializers.SerializerMethodField()

    class Meta:
        """
        This is the meta class that contains the serializer
        custom options.
        """
        model = Message
        fields = 'message_id', 'sender', 'sender_name', 'conversation'\
            'message_body', 'sent_at'

    def get_sender_name(self, obj):
        """
        This is a custom method on this serializer that get all
        sender full name
        """
        return f"{obj.sender.first_name} {obj.sender.last_name}"
