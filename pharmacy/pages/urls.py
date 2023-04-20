from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('admin',views.adminpage,name="adminpage"),
    path('prescription_upload/',views.prescription_upload,name="prescription_upload"),
    path('prescription_products/',views.prescription_products,name="prescription_products"), 

]