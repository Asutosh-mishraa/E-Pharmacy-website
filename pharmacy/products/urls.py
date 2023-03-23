from django.urls import path
from . import views

urlpatterns = [
    path('allproduct/',views.all_products,name="all_product"),
    path('details/<int:id/',views.product_detail,name="prod_detail"), 
]