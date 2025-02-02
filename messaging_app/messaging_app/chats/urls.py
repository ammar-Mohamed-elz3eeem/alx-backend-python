from rest_framework import routers
from .views import UsersViewSet, MessageViewSet, ConversationViewSet
from django.urls import include, path
from rest_framework_nested.routers import NestedDefaultRouter


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet, 'user')
router.register(r'conversations', ConversationViewSet, 'conversation')

conversation_router = NestedDefaultRouter(router, 'conversations',  
                                          lookup='conversations_id')

conversation_router.register(r'messages', MessageViewSet,
                             basename='conversation-messages')

urlpatterns = [
    path("", include(router.urls))
]
