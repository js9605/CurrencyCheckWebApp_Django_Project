from django.db import models
from .webscraper import scrape_website


class Currency(models.Model):
    currency_name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    ref_number = models.IntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=4) 
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4) 
    average_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)  

    @classmethod
    def save_data(cls):
        currencies = ["USD", "CHF"]
        for currency in currencies:
            scraped_data = scrape_website(currency)
            currency_instance = cls(
                currency_name=scraped_data.get('currency_name'),
                country=scraped_data.get('country'),
                ref_number=scraped_data.get('ref_number'),
                purchase_rate=scraped_data.get('purchase_rate'),
                selling_rate=scraped_data.get('selling_rate'),
                average_exchange_rate=scraped_data.get('average_exchange_rate')
            )
            currency_instance.save()

    def __str__(self):
        return self.currency_name
