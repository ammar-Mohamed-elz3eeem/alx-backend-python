from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import action 
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Message, Conversation
from .serializers import UserSerializer,\
    MessageSerializer, ConversationSerializer
from .filters import MessageFilter
from .permissions import IsParticipantOfConversation


class UsersViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the Message model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['conversation', 'sender']
    filterset_class = MessageFilter


class ConversationViewSet(viewsets.ModelViewSet):
    """
    This is the viewset responsible for showing data
    from the Conversation model
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['participants']
    permission_classes = [IsParticipantOfConversation]

    @action(['get'], True)
    def messages(self, request, pk=None):
        """
        Custom action method that retrives all messages that
        exist in the current conversation.
        """
        conversation = self.get_object()
        messages = Message.objects.filter(conversation=conversation)
        serializer = MessageSerializer(messages, many=True)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)
