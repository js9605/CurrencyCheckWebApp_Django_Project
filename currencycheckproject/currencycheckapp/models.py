from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    user = models.ForeignKey(User, related_name='currencies', on_delete=models.CASCADE, null=True)
    currency_shortcut = models.CharField(max_length=50)
    country = models.CharField(max_length=150)
    ref_number = models.IntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=4)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4)
    average_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    stored_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.currency_shortcut
    

class UserCurrencies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency_shortcut = models.CharField(max_length=50)
    upper_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lower_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.currency_shortcut

