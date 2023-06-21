from django.db import models
class Order(models.Model):
    products = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=50)

# Create your models here.
