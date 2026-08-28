from django.db import models

# Create your models here.
from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    street_name = models.CharField(max_length=255)
    town_city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.town_city}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='store/images/')

    def __str__(self):
        return self.title