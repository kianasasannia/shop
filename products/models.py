from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)

class Product (models.Model):
    name= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=15,decimal_places=0)
    available=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="product_images/",blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
