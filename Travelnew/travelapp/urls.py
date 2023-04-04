from django.urls import path
from . import views

urlpatterns=[
    path('adddestination/',views.adddestination,name='adddestination'),
    path('redestination/',views.redestination,name='redestination'),
    path('viewdestination/',views.viewdestination,name='viewdestination'),
    path('editdestination/<int:destid>/',views.editdestination,name='editdestination'),
    path('updatedestination/<int:destid>/',views.updatedestination,name='updatedestination'),
    path('deletedestination/<int:destid>/',views.deletedestination,name='deletedestination'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('viewcontact/',views.viewcontact,name='viewcontact')
]