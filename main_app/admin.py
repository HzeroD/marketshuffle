from django.contrib import admin
from .models import Stock, Client,Order

# Register your models here
admin.site.register(Stock)
admin.site.register(Client)
admin.site.register(Order)