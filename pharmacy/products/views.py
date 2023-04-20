from django.shortcuts import render

from .models import product

def all_products(request):
    products = product.objects.all()
    context = {
        "products":products
    }
    return render(request,'products/allprod.html', context)
def product_detail(request):
    # products=product.objects.get(id=id)
    # context={
    #     'products' : products,
    # }
    return render(request,'products/prod_details.html')
def search(request):
    product_name=request.GET.get("search")
    search_result=product.objects.filter(name__icontains=product_name)

    context={
        "search_result": search_result
    }
    return render(request,'products/search.html',context)

def cart(request):
    return render(request,'products/cart.html')
def checkout(request):
    return render(request,'products/checkout.html')