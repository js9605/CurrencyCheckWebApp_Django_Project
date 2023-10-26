from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Currency(models.Model):
    currency_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    ref_number = models.IntegerField()
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=4)
    selling_rate = models.DecimalField(max_digits=10, decimal_places=4)
    average_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    spread = models.DecimalField(max_digits=10, decimal_places=4)
    value = models.DecimalField(max_digits=10, decimal_places=4) 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currencies = models.ManyToManyField(Currency)

    def __str__(self):
        return self.user.username