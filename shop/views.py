from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Child_Category,Category
import json
from .forms import ProductForm,CategoryForm,Chid_CategoryForm
# Create your views here.
from django.http import HttpResponse
def category(request):
    categorys = Category.objects.all()
    child_categorys = Child_Category.objects.all()
    f =[]
    for i in categorys:
        category = i
        d = {}
        e = []
        d['category']=category.category_name
        d['id']=i.id
        for x in child_categorys:

            if category.id == x.category_id:

                e.append(x.child_category_name)
        d['childcategory']= e
        f.append(d)

    return render(request,'categorys.html',{'categorys':f})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'products': form})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorys')
    else:
        form = CategoryForm()
    return render(request, 'category_create.html', {'category': form})


def child_category_create(request):
    if request.method == 'POST':
        form = Chid_CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorys')
    else:
        form = Chid_CategoryForm()
    return render(request, 'child_category_create.html', {'category': form})