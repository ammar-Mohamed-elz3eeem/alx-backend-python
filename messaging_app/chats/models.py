from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid


class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin')
    )
    id = models.UUIDField(db_column='user_id',
                          primary_key=True,
                          default=uuid.uuid4)
    password = models.CharField(db_column='password_hash', max_length=100)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES,
                            default='guest')
    date_joined = models.DateTimeField(db_column='created_at',
                                       default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'users'


class Conversation(models.Model):
    id = models.UUIDField(db_column='conversation_id',
                          primary_key=True,
                          default=uuid.uuid4)
    participants = models.ForeignKey(User,
                                        on_delete=models.CASCADE,
                                        related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'conversations'


class Message(models.Model):
    id = models.UUIDField(db_column='message_id',
                          primary_key=True,
                          default=uuid.uuid4)
    sender = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name="messages_sent")
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    conversations = models.ManyToManyField(Conversation, related_name='messages')

    class Meta:
        db_table = 'messages'
