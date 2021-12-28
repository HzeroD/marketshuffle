from django.db import models

# Import the User
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    name: models.CharField(max_length=50)
    worth: models.FloatField()
    

class Stock(models.Model):
    name: models.CharField(max_length=50)
    ticker: models.CharField(max_length=20)
    purchase_price: models.FloatField()

    clients = models.ManyToManyField(Client)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Order(models.Model):
    date: models.DateField('Sell Date')
    qty: models.IntegerField()
    stock: models.ForeignKey(Stock, on_delete=models.CASCADE)

