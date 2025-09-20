from django.contrib import admin
from .models import *

class Product_admin (admin.ModelAdmin):
    list_display=("name","price","available","category")
    list_filter=("available","category")
    search_fields=("name",)

class Category_admin (admin.ModelAdmin):
    list_display=("name",)

admin.site.register(Product,Product_admin)
admin.site.register(Category,Category_admin)
