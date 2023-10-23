from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='UserModel')

urlpatterns = router.urls