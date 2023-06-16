from django import forms
from .models import Product,Child_Category,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'category','child_category_name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields =['category_name']

class Chid_CategoryForm(forms.ModelForm):
    class Meta:
        model = Child_Category
        fields = ['category','child_category_name']