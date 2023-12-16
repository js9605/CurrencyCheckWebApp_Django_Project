# from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView, ListUserCurrenciesView, DeleteUserCurrenciesView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
    path('list_user_currencies/', ListUserCurrenciesView.as_view(), name='list-user-currencies'),
    path('delete_user_currency/<int:pk>/', DeleteUserCurrenciesView.as_view(), name='delete-user-currency'),
    ]


# TODO MAIN
# 1 (DONE) Fix EUR parsing 
# 2 (DONE) Add "go back to LoadCurrencyData" on Display site and the other way "go to LoadCurrencyDataView"
# 3 (DONE) Save previously added currencies so User dont need to name the 
# ones for scraping at that moment
# - Append new currencies in currency_shortcut (handle duplicates, how to delete unwanted currencies?)
# 4 (DONE) Add deletion of currencies in list_user_currencies/
# 5 (DONE) Add automatic scraping after entering /display_currencies/ url
# 6 (DONE) Add validation (did user provided the correct names of the currency?)
# 7 (DONE) Rename functions, variables, classes to be more descriptive
# 8 (DONE) User input currencies "toUpper"
# 9 (DONE) Use Docker
# 10 
# - (DONE) Send mail with notification about exceeted currency values
# - Ability to assign upper and lower limits for a specific currency
# - Testing these currency boundaries in real time
# 11 Logging with OAuth
# 12 Testing
# 13 Github Docs - Create understandable and professional usage documentation 