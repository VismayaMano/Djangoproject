from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages
from app1.forms import LoginForm,RegisterForm, UpdateForm, ChangePasswordForm
from .models import Gallery, Signup
from django.contrib.auth import logout as logouts

# Create your views here.



def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            photo=form.cleaned_data['Photo']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['Confirmpassword']

            user=Signup.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"Email already exist")
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,"password missmatch")
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Email=email,Photo=photo,Password=password)
                tab.save()
                messages.success(request,"data saved....")
                return redirect('/')

    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form})    


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Signup.objects.get(Email=email)

                if not user:
                    messages.warning(request,"Email doesnot exist")
                    return redirect('/login')

                elif password!=user.Password:
                    messages.warning(request,"incorrect password")
                    return redirect('/login')

                else:
                    messages.success(request,"login successfull")
                    return redirect('/home/%s' % user.id) 
            except:
                messages.warning(request,"incorrect password or email")
                return redirect('/login')

    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    user=Signup.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            form.save()
            messages.success(request,"data updated...")
            return redirect('/home/%s' % user.id) 
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user}) 

def passwordchange(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form= ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            confirmpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                messages.warning(request,"incorrect password...")
                return redirect('/passwordchange/%s' % user.id)
            elif newpassword!=confirmpassword:
                messages.warning(request,"password missmatch...")
                return redirect('/passwordchange/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"old and new passwords cannot be same....")
                return redirect('/passwordchange/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                return redirect('/home/%s' % user.id)
                message.success(request,"password changed successfully....")            

    else:
        form=ChangePasswordForm()
    return render(request,'passwordchange.html',{'form':form, 'user':user})

def logout(request):
    logouts(request)
    messages.success(request,"logout successfull")
    return redirect('/') 

def gallery(request):
    data=Gallery.objects.all()
    return render(request,'gallery.html',{'data':data})

def details(request,id):
    user=Gallery.objects.get(id=id)
    return render(request,'details.html',{'user':user})


