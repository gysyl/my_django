from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
