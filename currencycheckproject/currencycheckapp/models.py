from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    owner = models.ForeignKey(User, related_name='currencies', on_delete=models.CASCADE, null=True)
    currency_shortcut = models.CharField(max_length=50)
    country = models.CharField(max_length=150)
    ref_number = models.IntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=4)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4)
    average_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.currency_shortcut
    

class CurrenciesToScrape(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    currencies_to_scrape = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
