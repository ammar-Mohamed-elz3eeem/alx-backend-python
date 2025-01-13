from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    """
    This is a filter that filters messages that has happned
    on specifiec start_date and end_date.
    """
    start_date = filters.DateTimeFilter('sent_at', 'gte')
    end_date = filters.DateTimeFilter('sent_at', 'lte')

    class Meta:
        """
        This is a custom class to handle model and start_date
        and end_date.
        """
        model = Message
        fields = ['sender', 'start_date', 'end_date']
