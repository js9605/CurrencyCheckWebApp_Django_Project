from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .webscraper import scrape_website


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ScraperView(APIView):
    def get(self, request):
        if request.method == 'GET':
            scraped_data = scrape_website()
            return Response(scraped_data)