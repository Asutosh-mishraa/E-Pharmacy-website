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

def add_to_cart(request):
    if request.method =="POST":
        product_id=request.POST.get("product_id")
        quantity=request.POST.get("quantity")
        items={}
        if request.session.get("items"):
            items=request.session.get("items")
        items[product_id]=quantity
        request.session["items"]=items
        print(request.session["items"])
    return redirect('cart')

def cart(request):
    prod=request.session.get("items")
    items=[]
    total_price=0
    if prod:
        for id,quantity in prod.items():
            p=product.objects.get(id=id)
            price=int(quantity) * float(p.price)
            #perprice=int(prod.price)
            total_price += price
            price=round(price,2)
            total_price = round(total_price,2)
            items.append({
                "id" : id,
                "name" : p.name,
                "quantity" : quantity,
                "price" : price,
                "photo" : p.product_image,
                "perprice" : p.price,
            })
    request.session["totalcartitems"]=len(items)

    context={
        "products":items,
        "total_price": total_price,
    }
    return render(request,'products/cart.html',context)

def delete_cart_item(request, id):
    products=request.session.get("items")
    id=str(id)
    del products[id]
    request.session["items"] = products
    return redirect("cart")

def checkout(request):
    return render(request,'products/checkout.html')
def invoice(request):
    return render(request,'products/invoice.html')