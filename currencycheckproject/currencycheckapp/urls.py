from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataViewSet, DisplayCurrencyDataViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'currencies', DisplayCurrencyDataViewSet, basename='currency-display')
router.register(r'upload_currencies', LoadCurrencyDataViewSet, basename='currency-load')

urlpatterns = [
    # /api/currencies/
    # /api/currencies/custom_action/
    path('api/', include(router.urls)), #Add data validation for inserted list of currencies(str)
]
