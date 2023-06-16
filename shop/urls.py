from django.urls import path
from .views import category
from . import views
urlpatterns = [

    path('productdetails/', views.product_list, name='product_list'),
    path('categorys/',category,name= 'categorys'),
    path('create/category/',views.category_create, name= 'category_create'),
    path('create/childcategory/',views.child_category_create, name= 'childcategory_create'),
    path('details/<int:pk>', views.product_detail, name='product_detail'),
    path('create/product/', views.product_create, name='product_create'),
    path('update/<int:pk>', views.product_update, name='product_update'),
    path('delete/<int:pk>', views.product_delete, name='product_delete'),

]