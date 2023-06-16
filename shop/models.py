from django.db import models

# Create your models here.
class Category(models.Model):
    """
   Create category for the product

    """
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name
class Child_Category(models.Model):
    """
    Creating child category
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    child_category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.child_category_name

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    child_category_name = models.ForeignKey(Child_Category,null=True,blank=True,on_delete=models.CASCADE)