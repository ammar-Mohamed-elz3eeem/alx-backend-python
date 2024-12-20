from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Message, Conversation
from .serializers import UserSerializer,\
    MessageSerializer, ConversationSerializer
from rest_framework import permissions


class UsersViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the User model
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class MessageViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the Message model
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]


class ConversationViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the Conversation model
    """

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.AllowAny]
