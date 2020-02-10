from django.db import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=120)
    product_type=models.CharField(max_length=120)
    product_price=models.IntegerField()
