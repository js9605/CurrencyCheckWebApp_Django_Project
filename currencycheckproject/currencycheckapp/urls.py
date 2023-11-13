from rest_framework.routers import DefaultRouter
from .views import CurrencyView, homepage, UserRegistrationView
from django.urls import path


#TODO Use DefaultRouter?
urlpatterns = [
    path('home/', homepage),
    path('currency/<str:currency_codes>/', CurrencyView.as_view(), name='currency_view'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
