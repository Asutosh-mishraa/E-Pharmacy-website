from django.shortcuts import render,redirect
#from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import MyUser

# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        print(username,password)

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'user/login.html')

def register(request):

    if request.method == "POST":
        name= request.POST.get('name')        
        mobile= request.POST.get('mobile')
        email= request.POST.get('email')
        password= request.POST.get('password1')

        error=False
        if MyUser.objects.filter(email=email).exists():
            #print("Email Already Exists")
            messages.error(request,"Email Already Exists")
            error=True
        if error:
            return render(request,"user/register.html")
        else:
            try:
                user = MyUser.objects.create_user(
                    name=name,
                    email=email,
                    mobile=mobile,
                    password=password
                )
                user.save()
                #print("User Created")
                messages.success(request,"Account created Successfully. Login to continue")
                return redirect('signin')
            except Exception as e:
                print(e)

    return render(request, 'user/register.html')
def signout(request):
    logout(request)
    return redirect('signin')