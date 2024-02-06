from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from jobseeker.forms import Registration,StudentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from django.contrib.auth import authenticate,login,logout
from jobapp.models import Student,job,Applications
from django.utils.decorators import method_decorator
# Create your views here.

def Signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
        

class Register(CreateView):
    template_name ='jobseeker/register.html'
    form_class  = Registration
    model = User
    success_url = reverse_lazy("reg")

# class Signin(View):
#     def get(self,request,args,*kwargs):
#         form = LoginForm()
#         return render(request,"jobseeker/login.html",{"form":form})
    
#     def post(self,request,args,*kwargs):
#         form =  LoginForm(request.POST)
#         if form.is_valid():
#             u_name = form.cleaned_data.get("Username")
#             pwd = form.cleaned_data.get("Password")
#             user_obj = authenticate(username = u_name,password = pwd)
#             if user_obj:
#                 login(request,user_obj)
#                 print("User logged in")

#             else:
#                 print("False Credentials")

#         return redirect("reg")

@method_decorator(Signin_required,name="dispatch")
class Student_home(ListView):
    template_name = "jobseeker/index.html"
    model=job
    context_object_name="job"

class Profile(CreateView):
    template_name = "jobseeker/seekerprofile.html"
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy("reg")

    # def post(self,request,*args,**kwargs):
    #     form=StudentForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("index")
    #     else:
    #         print("getout")
    #     return redirect("reg")

    def form_valid(self, form: BaseModelForm):
        form.instance.user=self.request.user
        return super().form_valid(form)
@method_decorator(Signin_required,name="dispatch")   
class ProfileView(DetailView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     data=Student.objects.filter(id=id)
    #     return render (request,"jobseeker/profileview.html",{"data":data})
    template_name="jobseeker/profileview.html"
    context_object_name="data"
    model=Student
@method_decorator(Signin_required,name="dispatch")
class UpdateProfile(UpdateView):
    template_name ='jobseeker/profile_edit.html'
    model = Student
    form_class  = StudentForm
    success_url = reverse_lazy("reg")

class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
@method_decorator(Signin_required,name="dispatch")
class JobDetailview(DetailView):
    template_name="jobseeker/job_detail.html"
    model=job
    context_object_name='data'
@method_decorator(Signin_required,name="dispatch")
class ApplyJobview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        data=job.objects.get(id=id)
        Applications.objects.create(jobs=data,student=request.user)
        return redirect("seekerindex")

    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     job_obj=job.objects.get(id=id)
    #     user=request.user
    #     Applications.objects.create(jobs=job_obj,student=user)
    #     return redirect("seekerindex")
@method_decorator(Signin_required,name="dispatch")
class Applied_jobs(View):
    def get(self,request,*args,**kwargs):
        data=Applications.objects.filter(student=request.user)
        return render(request,"jobseeker/jobapplied.html",{"data":data})
@method_decorator(Signin_required,name="dispatch")
class Delete_job(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Applications.objects.get(id=id).delete()
        return redirect("seekerindex")








