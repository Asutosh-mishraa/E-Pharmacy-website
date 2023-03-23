from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def allprod(request):
    return render(request,'pages/allprod.html')
def adminpage(request):
    return render(request,'admin/base_site.html')