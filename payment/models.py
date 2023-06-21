from django.db import models

class Payment(models.Model):
    customer_name = models.CharField(max_length=255)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=255)
    payment_description = models.TextField()
    payment_method_name = models.CharField(max_length=255)


# Create your models here.
