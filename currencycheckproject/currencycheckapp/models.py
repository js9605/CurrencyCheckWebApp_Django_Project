from django.db import models
from .webscraper import scrape_website


class Currency(models.Model):
    currency_name = models.CharField(max_length=120)
    currency_shortcut = models.CharField(max_length=3, default='USD')
    country = models.CharField(max_length=150)
    ref_number = models.IntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=4) 
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4) 
    average_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)  

    @classmethod
    def save_data(cls, currencies):
        
        #TODO
        # http://127.0.0.1:8000/currency/EUR/ -> HTTP 200 OK but returns USD
        # If you are indeed passing "EUR" in the URL, but it's not being captured in the view, there might be an issue with your URL configuration or how you are making the request. Double-check the URL you are accessing in your browser or through your frontend application to ensure it's correctly passing the currency_codes parameter.
        # Additionally, in your save_data function, make sure to handle the case where the scrape_website function does not return valid data for the provided currency code. If the extract_currency function does not find the expected elements, it might return an empty dictionary, which could cause issues when creating the Currency instance. Consider adding validation checks before creating and saving the Currency instance to handle such cases gracefully.

        for currency in currencies:
            scraped_data = scrape_website(currency)

            print("HERE", scraped_data)

            currency_instance = cls(
                currency_name=scraped_data.get('currency_name'),
                currency_shortcut=scraped_data.get('currency_shortcut'),
                country=scraped_data.get('country'),
                ref_number=scraped_data.get('ref_number'),
                purchase_rate=scraped_data.get('purchase_rate'),
                selling_rate=scraped_data.get('selling_rate'),
                average_exchange_rate=scraped_data.get('average_exchange_rate')
            )
            currency_instance.save()

    def __str__(self):
        return self.currency_name
