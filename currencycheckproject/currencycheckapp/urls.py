from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, CurrenciesToScrapeViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'upload_currencies', CurrenciesToScrapeViewSet, basename='currency')

urlpatterns = [
    # /api/currencies/
    # /api/currencies/custom_action/
    path('api/', include(router.urls)), #Add data validation for inserted list of currencies(str)
]
