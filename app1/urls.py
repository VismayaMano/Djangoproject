from django.urls import path

from app1.models import Gallery
from .import views

app_name='app1'
urlpatterns=[

    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('gallery',views.gallery,name='gallery'),
    path('details/<int:id>',views.details,name='details'),
    path('passwordchange/<int:id>',views.passwordchange,name='passwordchange'),
    path('logout',views.logout,name='logout'),
    
    ]