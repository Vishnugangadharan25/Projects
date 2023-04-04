from django.urls import path
from . import views

urlpatterns=[
    path('userlogin/',views.userlogin,name='userlogin'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('uregister/',views.uregister,name='uregister'),
    path('ulogin/',views.ulogin,name='ulogin'),
    path('ucontact/',views.ucontact,name='ucontact'),
    path('userlogout/',views.userlogout,name='userlogout')
]