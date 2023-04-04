from django.shortcuts import render,redirect
from travelapp.models import Destination
from . models import Register
from . models import Contact

# Create your views here.
def ulogin(request):
    return render(request,"login.html")
def userlogin(request):
    if request.method == "POST":
        uusername = request.POST.get('user')
        upassword = request.POST.get('pass')
        if Register.objects.filter(m_username=uusername,m_password=upassword).exists():
            data = Register.objects.filter(m_username=uusername,m_password=upassword).values('m_email','m_phone','id').first()
            request.session['nphone'] = data['m_phone']
            request.session['nemail'] = data['m_email']
            request.session['nusername'] = uusername
            request.session['npassword'] = upassword
            request.session['uid'] = data['id']
            return redirect('home')
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
def register(request):
    return render(request,"Register.html")
def uregister(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        Email=request.POST.get('email')
        Phonenum=request.POST['number']
        data=Register(m_username=username,m_password=password,m_email=Email,m_phone=Phonenum)
        data.save()
        return redirect('ulogin')
def home(request):
    data=Destination.objects.all()
    return render(request,"home.html",{"data":data})
def contact(request):
    return render(request,"contact.html")
def ucontact(request):
    if request.method=="POST":
        Name=request.POST['name']
        Email=request.POST['uemail']
        Message=request.POST['message']
        Subject=request.POST['subject']
        data=Contact(name=Name,email=Email,message=Message,subject=Subject)
        data.save()
    return redirect('home')
def about(request):
    return render(request,"about.html")
def userlogout(request):
    del request.session['nphone']
    del request.session['nemail']
    del request.session['nusername']
    del request.session['npassword']
    del request.session['uid']
    return redirect('ulogin')