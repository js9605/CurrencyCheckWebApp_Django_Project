from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.homepage),
    path('currency/<str:currency_codes>/', views.CurrencyView.as_view(), name='currency_view'),
]
