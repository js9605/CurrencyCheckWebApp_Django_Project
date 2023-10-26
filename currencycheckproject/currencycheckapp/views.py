from rest_framework import viewsets

from .models import User, Currency, UserProfile
from .serializers import UserSerializer, CurrencySerializer, UserProfileSerializer
from .webscraper import scrape_website


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# class ScraperView(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             scraped_data = scrape_website()
#             return Response(scraped_data)