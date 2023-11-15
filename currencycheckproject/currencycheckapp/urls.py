from rest_framework.routers import DefaultRouter
from .views import CurrencyView, homepage, UserRegistrationView, set_currencies_to_scrape
from django.urls import path


#TODO Use DefaultRouter?
urlpatterns = [
    path('home/', homepage),
    path('currency/<str:currency_codes>/', CurrencyView.as_view(), name='currency-view'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('user/', set_currencies_to_scrape, name='user-view-data'),

]
