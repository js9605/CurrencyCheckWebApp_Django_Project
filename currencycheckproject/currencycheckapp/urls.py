from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView
from django.urls import path


urlpatterns = [
    path('display_currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
]


# TODO MAIN
# Display saved currencies for specific user
# Send mail if currency treshold is exceeded (up/down treshold)


# TODO fix
# Scraper performs scraping twice by which calling one currency 
# once saves two values in "display" url

# Information about the saved date and time of currency scraping 
# does not display on the "display" url\

