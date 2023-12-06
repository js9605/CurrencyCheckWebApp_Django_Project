from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
]


# TODO MAIN
# 1 (DONE) Fix EUR parsing 
# 2 (DONE) Add "go back to LoadCurrencyData" on Display site and the other way "go to LoadCurrencyDataView"
# 3 Save previously added currencies so User dont need to name the 
# ones for scraping at that moment
# 3 Add validation (did user provided the correct names of the currency?)
# 4 Use Docker
# 5 Make frontend prettier
# 6 Logging with OAuth
# 7 Send mail with notification about exceeted currency values
# - Ability to assign upper and lower limits for a specific currency
# - Testing these currency boundaries in real time
# 8 Testing
# 9 Github Docs - Create understandable and professional usage documentation 