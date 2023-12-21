from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('abouts/',views.abouts,name='abouts'),
    path('contactus/',views.contactus,name='contactus'),
    path('login/',views.login,name='login'),
   
    path('registration/',views.registration,name='registration'),

]