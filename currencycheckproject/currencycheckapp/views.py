from .serializers import CurrencySerializer
from .models import Currency, UserCurrency
from .services.data_loader import save_currency_data, update_currency_list

from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class DisplayCurrencyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        save_currency_data(request.user)

        self.delete_old_currencies(request.user)

        user_currencies = Currency.objects.filter(user=request.user)
        serializer = CurrencySerializer(user_currencies, many=True)

        return render(request, 'display_exchange_rates.html', {'currencies': serializer.data, 'user': request.user})

    def delete_old_currencies(self, user):
        cutoff_date = timezone.now() - timezone.timedelta(weeks=1)
        Currency.objects.filter(user=user, stored_date__lt=cutoff_date).delete()


class LoadCurrencyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return render(request, 'load_currency_data.html', {'user': request.user})

    def post(self, request, *args, **kwargs):
        currencies_to_scrape = request.data.get('currencies_to_scrape', 'key_is_not_found').strip()

        if currencies_to_scrape:
            update_currency_list(currencies_to_scrape, request.user)
            return render(request, 'load_currency_data.html', {'user': request.user})
        else:
            return Response({'error': 'Currencies cannot be empty.'}, status=400)


class DeleteUserCurrencyView(View):
    def post(self, request, pk, *args, **kwargs):
        currency = get_object_or_404(UserCurrency, pk=pk)
        currency.delete()
        return HttpResponseRedirect(reverse('list_user_currencies'))
    
def list_user_currencies(request):
    user = request.user
    user_currencies = UserCurrency.objects.filter(user=user)

    return render(request, 'list_user_currencies.html', {'user_currencies': user_currencies, 'user': user})