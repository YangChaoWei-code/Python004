from django.db import models


class PhoneComment(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField(max_length=50)
    content = models.CharField(max_length=200)
    sentiment = models.FloatField(max_length=50)
# Create your models here.
