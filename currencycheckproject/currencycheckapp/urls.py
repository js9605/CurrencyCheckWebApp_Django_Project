# from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView, ListUserCurrenciesView, DeleteUserCurrenciesView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
    path('list_user_currencies/', ListUserCurrenciesView.as_view(), name='list-user-currencies'),
    path('delete_user_currency/<int:pk>/', DeleteUserCurrenciesView.as_view(), name='delete-user-currency'),
    ]


