from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,UpdateView
from django.contrib.auth import authenticate,login,logout
from Hrapp.forms import LoginForm,CategoryForm,JobForm
from django.urls import reverse_lazy 
from jobapp.models import Category,job,Applications
# Create your views here.


class Loginview(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                if request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("seekerindex")
            else:
                print("failed")
            return render(request,"login.html",{"form":form})
class dashboard(TemplateView):
    template_name="index.html"

class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
    
class AddCategory(CreateView,ListView):
    template_name="category.html"
    form_class=CategoryForm
    success_url=reverse_lazy("category")
    context_object_name="data"
    model=Category

class CategoryRemove(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Category.objects.get(id=id).delete()
        return redirect("category")
    
class AddJob(CreateView):
    template_name="job_add.html"
    form_class=JobForm
    model=job
    success_url=reverse_lazy("addjob")
    context_object_name=('qs')

class DeleteJob(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        job.objects.filter(id=id).delete()
        return redirect("joblist")

class JobDetail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=job.objects.filter(id=id)
        return render(request,"jobview.html",{"qs":qs})
    
class JobList(ListView):
    template_name="joblist.html"
    model=job
    context_object_name="jobs"

class JobUpdate(UpdateView):
    template_name="jobupdate.html"
    form_class=JobForm
    model=job
    success_url=reverse_lazy("joblist")

class View_appliedjobs(View):
    def get(self,request,*args,**kwargs):
        data=Applications.objects.all()
        return render(request,"viewappliedjobs.html",{"data":data})

class Logout(View):
    def get(self,request,*args,**kwargs):
        logout=request
        return redirect("login")

