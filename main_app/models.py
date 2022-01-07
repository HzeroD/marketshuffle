import datetime
from django.db import models
from django.urls import reverse
from datetime import date,time
from django.utils import timezone
from django.db.models import Q


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
    qty = models.IntegerField(default=100)
    market_cap = models.CharField(max_length=20)

    clients = models.ManyToManyField(Client)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("stocks_detail", kwargs={"stock_id": self.id})

class Order(models.Model):
    date = models.DateField('Sell Date')
    time = models.TimeField()
    qty = models.IntegerField(default=1)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} on {self.qty}"
        
    # def order_pending(self):
    #     return Order.objects.filter(Q(date__gt=datetime.datetime.now().date()),
    #     Q(time__gte=datetime.datetime.now().time()) | Q(date__gt=datetime.datetime.now().date())).order_by('-date')