from django.shortcuts import render,redirect
from django.views.generic import View
from jobapp.forms import HrRegister,HrLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
class HrRegisterView(View):
    def get(self,request,*args,**kwargs):
        form=HrRegister()
        return render(request,'reg.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=HrRegister(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
        return render(request,'reg.html',{"form":form})
class HrLoginView(View):
    def get(self,request,*args,**kwargs):
        form=HrLogin()
        return render(request,'login.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=HrLogin(request.POST)
        if form.is_valid():
           uname=request.Post.get("username")
           pwd=request.POST.get("password")
           user_obj=authenticate(request,usernmae=uname,password=pwd)
           print(user_obj)
           if user_obj:
               login(request,user_obj)
               return redirect("reg")
           else:
               print("invalid")
        return render(request,'login.html',{"form":form})
