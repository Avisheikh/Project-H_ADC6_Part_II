from django.db import models
from store.models import product
from django.contrib.auth.models import User
# Create your models here.
class order(models.Model):
    products = models.OneToOneField(product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.products.Product_Name

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(order)
   

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.products.Product_Price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.user)


    
