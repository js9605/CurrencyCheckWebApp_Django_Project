from rest_framework.routers import DefaultRouter
from .views import ScraperView, UserViewSet
from django.urls import path, include


# router = DefaultRouter()
# router.register(r'user', UserViewSet, basename='UserModel')
# urlpatterns = router.urls

urlpatterns = [
    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user'),
    path('scrape/', ScraperView.as_view(), name='scraped-data'),
]