from .serializers import CurrencySerializer
from .models import Currency, UserCurrencies
from .services.data_loader import scrape_currency_data, update_user_currencies_list
from .utils.currency_codes import VALID_CURRENCY_CODES
from .forms import CurrencyLimitForm, AddUserCurrencyForm

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
        scrape_currency_data(request.user)

        self.delete_old_currencies(request.user)

        user_currencies = Currency.objects.filter(user=request.user)
        serializer = CurrencySerializer(user_currencies, many=True)

        return render(request, 'display_exchange_rates.html', {'currencies': serializer.data, 'user': request.user})

    def delete_old_currencies(self, user):
        cutoff_date = timezone.now() - timezone.timedelta(days=3)
        Currency.objects.filter(user=user, stored_date__lt=cutoff_date).delete()


class LoadCurrencyDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return render(request, 'load_currency_data.html', {'user': request.user})

    def post(self, request, *args, **kwargs):
        currencies_to_scrape = request.data.get('currencies_to_scrape', 'key_is_not_found').strip().upper()

        invalid_currencies = [currency.strip() for currency in currencies_to_scrape.split(',') if currency not in VALID_CURRENCY_CODES]

        if invalid_currencies:
            error_message = f"Invalid currency codes: {', '.join(invalid_currencies)}"
            return Response({'error': error_message}, status=400)

        if currencies_to_scrape:
            update_user_currencies_list(currencies_to_scrape, request.user)
            return render(request, 'load_currency_data.html', {'user': request.user})
        else:
            return Response({'error': 'Currencies cannot be empty.'}, status=400)


class DeleteUserCurrenciesView(View):
    def post(self, request, pk, *args, **kwargs):
        currency = get_object_or_404(UserCurrencies, pk=pk)
        currency.delete()
        return HttpResponseRedirect(reverse('list-user-currencies'))
    

# TODO Read email(template) and save it to model
class ListUserCurrenciesView(APIView):
    def get(self, request, *args, **kwargs):
        user_currencies = UserCurrencies.objects.filter(user=request.user)
        form = CurrencyLimitForm()
        return render(request, 'list_user_currencies.html', {'user_currencies': user_currencies, 'user': request.user, 'form': form})

    def post(self, request, *args, **kwargs):
        user_currencies = UserCurrencies.objects.filter(user=request.user)
        form = CurrencyLimitForm(request.POST)

        if form.is_valid():
            currency_id = request.POST.get('currency_id')
            currency = get_object_or_404(UserCurrencies, pk=currency_id)

            if request.POST.get('action') == 'set_limits':
                currency.upper_limit = form.cleaned_data['upper_limit']
                currency.lower_limit = form.cleaned_data['lower_limit']
                currency.save()
        else:
            print("DEBUG: form errors:", form.errors)

        return render(request, 'list_user_currencies.html', {'user_currencies': user_currencies, 'user': request.user, 'form': form})