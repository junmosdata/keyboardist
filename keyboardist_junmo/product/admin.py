from django.contrib import admin
from product.models import *

# Register your models here.

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'content')