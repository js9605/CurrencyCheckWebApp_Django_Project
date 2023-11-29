from rest_framework.routers import DefaultRouter
from .views import LoadCurrencyDataView, DisplayCurrencyDataView
from django.urls import path


urlpatterns = [
    path('currencies/', DisplayCurrencyDataView.as_view(), name='currency-display'),
    path('upload_currencies/', LoadCurrencyDataView.as_view(), name='currency-load'),
]


# router = DefaultRouter()
# router.register(r'currencies', DisplayCurrencyDataViewSet, basename='currency-display')
# router.register(r'upload_currencies', LoadCurrencyDataView, basename='currency-load')

# urlpatterns = [
#     path('', include(router.urls)),
# ]




#TODO MAIN
# Change ModelViewSet to APIview
# Display saved currencies for specific user
# Send mail if currency treshold is exceeded (up/down treshold)

# Check serializer.is_valid()
