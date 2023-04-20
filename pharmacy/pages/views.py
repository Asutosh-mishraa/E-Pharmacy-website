from django.shortcuts import render
from products.models import category

# Create your views here.
def index(request):
    categories=category.objects.all()
    context={
        'categories' : categories,
    }
    return render(request,'pages/index.html',context)
def allprod(request):
    return render(request,'pages/allprod.html')
def adminpage(request):
    return render(request,'admin/base_site.html')