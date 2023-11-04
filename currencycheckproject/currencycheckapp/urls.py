from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


urlpatterns = [
    path('home/', views.homepage),
    path('currency/', views.currency_view),
]