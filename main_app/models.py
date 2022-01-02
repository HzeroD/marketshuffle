from django.db import models
from django.urls import reverse

# Import the User
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    worth = models.FloatField()

    def get_absolute_url(self):
        return reverse("clients_detail", kwargs={"pk": self.id})
    

class Stock(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=20)
    purchase_price = models.FloatField()
    volume = models.FloatField()

    clients = models.ManyToManyField(Client)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("stocks_detail", kwargs={"stock_id": self.id})

class Order(models.Model):
    date = models.DateTimeField('Sell Date/Time')
    qty = models.IntegerField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

