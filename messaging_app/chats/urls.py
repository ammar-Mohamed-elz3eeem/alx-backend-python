from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, MessageViewSet, ConversationViewSet


router = DefaultRouter()
router.register(r'users', UsersViewSet, 'user')
router.register(r'messages', MessageViewSet, 'message')
router.register(r'conversations', ConversationViewSet, 'conversation')

urlpatterns = router.urls
