from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataViewSet, DisplayCurrencyDataViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'currencies', DisplayCurrencyDataViewSet, basename='currency-display')
router.register(r'upload_currencies', LoadCurrencyDataViewSet, basename='currency-load')

urlpatterns = [
    path('', include(router.urls)),
]


#TODO MAIN
# Display saved currencies for specific user
# Send mail if currency treshold is exceeded (up/down treshold)

# Check serializer.is_valid() - how does it work?
