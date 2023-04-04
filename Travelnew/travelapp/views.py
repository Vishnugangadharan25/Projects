from django.shortcuts import render,redirect
from . models import Destination
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from UserApp.models import Contact
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.
def redestination(request):
    return render(request,"addDestination.html")
def adddestination(request):
    if request.method=="POST":
        destination_Name=request.POST['dname']
        destination_Description=request.POST['description']
        destination_Price=request.POST['price']
        destination_Image=request.FILES['image']
        data=Destination(destinationName=destination_Name,destinationDescription=destination_Description,destinationPrice=destination_Price,destinationImage=destination_Image)
        data.save()
    return redirect('viewdestination')
def viewdestination(request):
    data=Destination.objects.all()
    return render(request,"viewDestination.html",{"data":data})
def editdestination(request,destid):
    data=Destination.objects.filter(id=destid)
    return render(request,"Editdestination.html",{"data":data})
def updatedestination(request,destid):
    if request.method=="POST":
        destination_Name=request.POST['dname']
        destination_Description=request.POST['description']
        destination_Price=request.POST['price']
        try:
             Image = request.FILES['image']
             fs=FileSystemStorage()
             file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file= Destination.objects.get(id=destid).destinationImage
        Destination.objects.filter(id=destid).update(destinationName=destination_Name,destinationDescription=destination_Description,destinationPrice=destination_Price,destinationImage=file)
    return redirect('viewdestination')
def deletedestination(request,destid):
    Destination.objects.filter(id=destid).delete()
    return redirect('viewdestination')
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            request.session['username_a'] = username
            request.session['password_a'] = password
            return redirect('adddestination')
        else:
            return render(request,'adminlogin.html', {'msg':'Sorry Invalid User Credentials'})
    return render(request,'adminlogin.html')
def viewcontact(request):
     data=Contact.objects.all()
     return render(request,"message.html",{"data":data})

     
