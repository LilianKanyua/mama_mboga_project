from django.db import models

class Reviews(models.Model):
    product_name = models.CharField(max_length=255)
    ratings = models.IntegerField()
    date_posted = models.DateField()
    title = models.CharField(max_length=255)
# Create your models here.
