from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    """
    This is a custom permission class that checks if the user
    is already participant in the current conversation or not.
    """

    def has_object_permission(self, request, view, obj):
        """
        This method check if there is a current user registered
        and that user did participated in the conversation.
        """
        if not request.user.is_authenticated:
            return False
        return request.user in obj.participants.all()

    def has_permission(self, request, view):
        """
        This method check if there is a current user registered
        or not to grant him permission to see all conversations.
        """
        if not request.user.is_authenticated:
            return False
        return True
