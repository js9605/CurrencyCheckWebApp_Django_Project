from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView, list_user_currencies
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
    path('list_user_currencies/', list_user_currencies, name='list_user_currencies'),
    ]


# TODO MAIN
# 1 (DONE) Fix EUR parsing 
# 2 (DONE) Add "go back to LoadCurrencyData" on Display site and the other way "go to LoadCurrencyDataView"
# 3 (DONE) Save previously added currencies so User dont need to name the 
# ones for scraping at that moment
# - Append new currencies in currency_shortcut (handle duplicates, how to delete unwanted currencies?)
# 4 Add deletion of currencies in list_user_currencies/
# 5 Add validation (did user provided the correct names of the currency?)
# 6 Use Docker
# 7 Make frontend prettier
# 8 Logging with OAuth
# 9 Send mail with notification about exceeted currency values
# - Ability to assign upper and lower limits for a specific currency
# - Testing these currency boundaries in real time
# 10 Testing
# 11 Github Docs - Create understandable and professional usage documentation 