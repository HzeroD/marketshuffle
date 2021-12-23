from django.db import models

# Import the User
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    name: models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
