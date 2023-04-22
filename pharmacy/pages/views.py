from django.shortcuts import render
from products.models import category
from PIL import Image
from pytesseract import pytesseract
from string import punctuation
from products.models import product

# Create your views here.
def index(request):
    categories=category.objects.values_list('id', 'category')
    categories = list(categories)
    print(categories)
    request.session['categories'] = categories
    # context={
    #     'categories' : categories,
    # }
    return render(request,'pages/index.html')

def allprod(request):
    return render(request,'pages/allprod.html')

def adminpage(request):
    return render(request,'admin/base_site.html')

def prescription_upload(request):
    return render(request,'pages\prescription_upload.html')

def prescription_products(request):
    f = request.FILES['myfile'] # here you get the files needed
    print(f.name)
    path_to_image = f
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img)
    lines = []
    for line in text.splitlines():
        line = ''.join(e for e in line if e not in punctuation)
        # re.sub('[^A-Za-z0-9 ]+', '', line)
        lines.append(line)
    lines = [l for l in lines if len(l)!=0]
    print(lines)
    lines.append("Paracetamol")
    lines.append("Paracetamol") 
    srch_rslt=[]
    not_found=[]
    for product_name in lines:
        search_result=product.objects.filter(name__icontains=product_name)
        if len(search_result)==0:
            not_found.append(product_name)
        srch_rslt.append(search_result)
    print(srch_rslt)
    # x=product.objects.filter(name__icontains=lines[3][0:3])
    # print(x)
    # print(len(lines[3]))
    # print(len("COQ LC Tablet 10'S"))

    context={
        "result": srch_rslt,
        'lines': lines,
        'not_found': not_found,
    }

    return render(request, 'pages\prescription_products.html', context)