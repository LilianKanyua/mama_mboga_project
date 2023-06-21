from django.contrib import admin
from .models import Reviews

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("product_name","ratings","date_posted","title")

# Register your models here.
