from django.urls import path
from . import views

urlpatterns = [
    path('allproduct/',views.all_products,name="all_product"),
    path('details/<int:id>/',views.product_detail,name="prod_detail"), 
    path('search/',views.search,name="search"),
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name="cart"),
    path('delete_cart_item/<int:id>/',views.delete_cart_item,name="delete_cart_item"),
    path('category/<int:id>/',views.categorywise,name="categorywise"),
    path('invoice/',views.invoice,name="invoice"),
    path('myorders/',views.orders,name="orders"),
    path('order_placed/',views.placed,name="placed"),

    path('place_order/',views.place_order,name="place_order"),
    path('payment_success/',views.payment_success,name="payment_success"),   





]