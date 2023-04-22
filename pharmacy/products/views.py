from django.shortcuts import render, redirect, get_object_or_404

from .models import product

def all_products(request):
    products = product.objects.all()
    context = {
        "products":products
    }
    return render(request,'products/allprod.html', context)

def categorywise(request,id):
    products=product.objects.filter(category=id)
    #products = get_object_or_404(product, product.category=cat)
    #print(products)
    context={
        'products' : products,
    }
    return render(request,'products/categorywise.html',context)

def product_detail(request,id):
    products=product.objects.get(id=id)
    context={
        'product' : products,
    }
    return render(request,'products/prod_details.html',context)
def search(request):
    product_name=request.GET.get("search")
    search_result=product.objects.filter(name__icontains=product_name)
    #print(search_result)
    context={
        "search_result": search_result
    }
    return render(request,'products/search.html',context)

def cart(request):
    return render(request,'products/cart.html')
def checkout(request):
    return render(request,'products/checkout.html')