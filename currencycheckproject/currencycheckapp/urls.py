# from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView, list_user_currencies, DeleteUserCurrencyView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
    path('list_user_currencies/', list_user_currencies, name='list-user-currencies'),
    path('delete_user_currency/<int:pk>/', DeleteUserCurrencyView.as_view(), name='delete-user-currency'),
    ]


# TODO MAIN
# 1 (DONE) Fix EUR parsing 
# 2 (DONE) Add "go back to LoadCurrencyData" on Display site and the other way "go to LoadCurrencyDataView"
# 3 (DONE) Save previously added currencies so User dont need to name the 
# ones for scraping at that moment
# - Append new currencies in currency_shortcut (handle duplicates, how to delete unwanted currencies?)
# 4 (DONE) Add deletion of currencies in list_user_currencies/
# 5 Add automatic scraping after entering /display_currencies/ url
# 6 Add validation (did user provided the correct names of the currency?)
# 7 Use Docker
# 8 Make frontend prettier
# 9 Logging with OAuth
# 10 Send mail with notification about exceeted currency values
# - Ability to assign upper and lower limits for a specific currency
# - Testing these currency boundaries in real time
# 11 Testing
# 12 Github Docs - Create understandable and professional usage documentation 