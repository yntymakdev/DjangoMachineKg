
from django.db import models
class Category(models.Model):
    category_name = models.CharField(max_length=16)

       description = models.TextField()
        price = models.DecimalField(max_digits=10,decimal_places=2)
   def __str__(self):
       return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)

video = models.FileField(upload_to='videos/', null=True, blank=True)


