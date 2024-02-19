from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import RedirectView
from .models import Currency, UserCurrencies
from .serializers import CurrencySerializer, UserCurrenciesSerializer
from .services.data_loader import scrape_currency_data, update_user_currencies_list
from .utils.currency_codes import VALID_CURRENCY_CODES
from django.db import transaction

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

class DeleteUserCurrenciesView(RedirectView):
    pattern_name = 'list-user-currencies'

    def get_object(self):
        return get_object_or_404(UserCurrencies, pk=self.kwargs['pk'])

    def get_redirect_url(self, *args, **kwargs):
        self.get_object().delete()
        return super().get_redirect_url(*args, **kwargs)

class ListUserCurrenciesView(APIView):
    template_name = 'list_user_currencies.html'

    def get(self, request, *args, **kwargs):
        user_currencies = UserCurrencies.objects.filter(user=request.user)
        serializer = UserCurrenciesSerializer(user_currencies, many=True)
        return render(request, self.template_name, {'user_currencies': serializer.data, 'user': request.user})

    def post(self, request):
        action = request.data.get('action', '')
        user_currencies = UserCurrencies.objects.filter(user=request.user)
        serializer = UserCurrenciesSerializer(data=request.data)

        if serializer.is_valid():
            if action == 'set_limits':
                self.handle_set_limits(request, user_currencies, serializer)
            elif action == 'update_user_email':
                self.handle_update_user_email(request, user_currencies, serializer)
        else:
            print('DEBUG: serializer error:', serializer.errors)

        return render(request, self.template_name, {'user_currencies': user_currencies, 'user': request.user})

    # TODO update limits here - check handle_update_user_email. Iterate user_currencies like in handle_update_user_email
    def handle_set_limits(self, request, user_currencies, serializer):
        currency_id = request.data.get('currency_id')
        print(f'DEBUG: set_limits for currency_id: {currency_id}')
        currency = get_object_or_404(UserCurrencies, pk=currency_id)

        currency.upper_limit = request.data.get('upper_limit')
        currency.lower_limit = request.data.get('lower_limit')

        serializer = UserCurrenciesSerializer(data=request.data, instance=currency)

        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
                currency.save()
                print("DEBUG: For ", currency.currency_shortcut, " currency.upper_limit =", currency.upper_limit, " currency.lower_limit =", currency.lower_limit, " currency_id: ", currency_id)
        else:
            print('DEBUG: serializer error:', serializer.errors)

    def handle_update_user_email(self, request, user_currencies, serializer):
        user_email = request.data.get('user_email')

        # I have to iterate over each UserCurrencies instance (for each saved currency) to be assigned the same email
        if not UserCurrencies.objects.filter(user=request.user, user_email=user_email).exists():
            with transaction.atomic():
                for user_currency in user_currencies:
                    user_currency.user_email = user_email
                    user_currency.save()

            print('DEBUG: User email updated successfully.')
        else:
            print('DEBUG: User email already in usage. Please provide a different email if you want to change it.')
