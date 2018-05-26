from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    product_price = models.IntegerField(default=5)
    gst = models.IntegerField(default=5)
    totalPrice = models.FloatField(null=True, blank=True)
    timestamp=models.CharField(max_length=100)
    # on submit click on the product entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('gst:index')