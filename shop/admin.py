from django.contrib import admin
from .models import Category,Child_Category,Product
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ["category_name"]
class AdminChild_Category(admin.ModelAdmin):
    list_display = ["child_category_name","category"]
class AdminProducts(admin.ModelAdmin):
    list_display = ["product_name","price"
                           ,"category","child_category_name"]
admin.site.register(Category, AdminCategory)
admin.site.register(Child_Category, AdminChild_Category)
admin.site.register(Product, AdminProducts)