from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import product,Order
from user.models import Address

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
    request.session["totalprice"] = total_price

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
def orders(request):
    return render(request,'products/orders.html')
def placed(request):
    return render(request,'products/placed.html')

def place_order(request):

    if request.method == "POST":
        name = request.POST.get('name')        
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        city = request.POST.get('city')
        addr_line1 = request.POST.get('address1')
        addr_line2 = request.POST.get('address2')
        pin = request.POST.get('pin')
        state = request.POST.get('state')
        payment_mode_cod = request.POST.get('selector1')
        payment_mode_rpay = request.POST.get('selector2')

        prod = request.session.get("items")
        total_price = request.session.get("totalprice")
        #print(name, phone_number, email, city,addr_line1,addr_line2,pin,state, payment_mode_cod,payment_mode_rpay)
        if payment_mode_cod:
            address = Address(
                user = request.user,
                addr_line1 = addr_line1,
                addr_line2 = addr_line2,
                pin = pin,
                city = city,
                state = state,
                phone_number = phone_number,
            )
            address.save()
            if prod:
                order_details = ""
                address = "" +f"{name},\n{addr_line1},\n{addr_line2},\n{city},{pin}\n{state}\n{phone_number}"
                for id,quantity in prod.items():
                    p = product.objects.get(id=id)
                    price = p.price * int(quantity)
                    price = round(price,2)
                    order_details += f"{p.name}  x  {quantity} ----- {quantity} x {p.price} ----- {price} \n"
                order=Order(
                    user=request.user,
                    address = address,
                    order_details=order_details,
                    total_price=total_price,
                    payment_mode = payment_mode_cod,
                )
                order.save()
                msg = ""
                msg = msg + f"Hi {name},\nYour order has been successfully placed.\nOrder details :\n{order_details}Total Order amount = {total_price}\n\nShipping Details :\n{address}\nThank You for Ordering from us, Your order will be delivered within 7 working days.\nHappy Shopping."
                #print(msg)
                send_mail(
                    "Order Confirmation from Medikart",
                    msg,
                    "asumishra25@gmail.com",
                    [request.user.email,],
                    fail_silently=False
                )
                del request.session["items"]

            return render(request,'products/placed.html')
        else:
            return render(request,'products/invoice.html')