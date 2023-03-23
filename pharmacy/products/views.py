from django.shortcuts import render

from .models import product

def all_products(request):
    products = product.objects.all()
    context = {
        "products":products
    }
    return render(request,'products/allprod.html', context)
def product_detail(request,id):
    products=product.objects.get(id=id)
    context={
        'products' : products,
    }
    return render(request,'products/prod_details.html',context)