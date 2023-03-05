
from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.signin,name='signin'),
    path('logout/',views.signout,name='signout'),
]
