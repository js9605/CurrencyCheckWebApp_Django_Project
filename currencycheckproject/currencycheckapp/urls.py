from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, CurrenciesToScrapeViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'upload_currencies', CurrenciesToScrapeViewSet, basename='currency')

urlpatterns = [
    #TODO scrap 2 popular currencies and display
    path('api/', include(router.urls)), #TODO download data
    # /api/currencies/
    # /api/currencies/custom_action/
]
