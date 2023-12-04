from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
]


# TODO MAIN
# 1 Fix EUR parsing 
# 2 Load data for scraping and display on the same site (Top values are latest data)
# 3 Add validation (did user provided the correct names of the currency?)
# 4 Use Docker
# 5 Make frontend prettier
# 6 Logging with OAuth
# 7 Send mail with notification about exceeted currency values
# - Ability to assign upper and lower limits for a specific currency
# - Testing these currency boundaries in real time
# 8 Testing
# 9 Github Docs - Create understandable and professional usage documentation


