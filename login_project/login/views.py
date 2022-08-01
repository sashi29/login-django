
from django.shortcuts import render,redirect
from django.contrib import messages  
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User 
from django.urls import reverse
from django.http.response import HttpResponseRedirect 
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
global data
data=dict() 
reg_data=dict()
# Create your views here.
def login_process(request):  
    if request.method=="POST": 
        username=request.POST['name']
        password=request.POST['password1']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return HttpResponseRedirect('home',{"user":user})
        else: 
            messages.error(request,'invalid username or password') 
            return render(request,'login.html')




    return render(request,'login.html')
def register(request): 
        if request.method=="POST": 
            name=request.POST["name"] 
            password1=request.POST["password1"]  
            password2=request.POST["password2"] 
            email=request.POST["email"] 
            reg_data["user"]=name 
            reg_data["password1"]=password1 
            reg_data["password2"]=password2
            reg_data["email"]=email 
            if password1!=password2:
                messages.success(request,'password not matching') 
                return redirect('reg')
            if name.isalnum(): 
                messages.warning(request,'user name must be alpha numeric')
                return redirect('reg') 
            if len(name)<4: 
                messages.warning(request,'user name is too short') 
                return redirect('reg') 
            if User.objects.filter(email=email): 
                messages.warning(request,'email already exists') 
                return redirect('reg')
            u=User.objects.create_user(username=name, email=email, password=password1)
            u.set_password=password1
            u.save() 
            messages.success(request,'account created successfully.') 
            return redirect('success')
        return render(request,'register.html')  
def home(request):  
    return render(request,'home.html') 
def logout_process(request): 
    logout(request)
    return redirect('log')

def successpage(request): 
    return render(request,'success.html') 
def change_password(request): 
    return render(request,'passwordchangedone.html')
