import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils import timezone


class User(AbstractUser):
    """
    This is the model for the database table `users`
    """
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin')
    )
    user_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(db_column='password_hash',
                                max_length=100)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES,
                            default='guest')
    date_joined = models.DateTimeField(db_column='created_at',
                                       default=timezone.now)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='chat_user_permissions'  # Change related_name to avoid clashes
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='chat_user_groups'  # Change related_name to avoid clashes
    )

    def __str__(self):
        """
        return the string representation of the User object
        """
        return f"{self.first_name} {self.last_name} ({self.email})"


class Conversation(models.Model):
    """
    This is the model for the database table `conversation`
    """
    conversation_id = models.UUIDField(primary_key=True,
                                       default=uuid.uuid4,
                                       editable=False)
    participants = models.ManyToManyField(User,
                                          related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This is the meta class that contains the table
        custom options.
        """
        db_table = 'conversations'

    def __str__(self):
        """
        return the string representation of the Conversation
        object
        """
        return f"Conversation {self.conversation_id}"


class Message(models.Model):
    """
    This is the model for the database table `messages`
    """
    message_id = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False)
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="sent_messages")
    conversation = models.ForeignKey(Conversation,
                                      on_delete=models.CASCADE,
                                      related_name='messages')
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This is the meta class that contains the table
        custom options.
        """
        db_table = 'messages'

    def __str__(self):
        """
        return the string representation of the Message
        object
        """
        return f"Message {self.message_id} From {self.sender}"
