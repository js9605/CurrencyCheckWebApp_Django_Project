from rest_framework.routers import DefaultRouter
from .views import CurrencyView, homepage
from django.urls import path, include

urlpatterns = [
    path('home/', homepage),
    path('currency/<str:currency_codes>/', CurrencyView.as_view(), name='currency_view'),
    # path('users/create/', CreateUserView.as_view()),
]
