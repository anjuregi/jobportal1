from django.urls import path
from Hrapp import views 
urlpatterns = [
    path('login',views.Loginview.as_view(),name="login"),
    path('index',views.dashboard.as_view(),name="index"),
    path('logout',views.Logout.as_view(),name="logout"),
    path('create/',views.AddCategory.as_view(),name="category"),
    path('delete/<int:pk>',views.CategoryRemove.as_view(),name="category-del"),
    path('jobadd/',views.AddJob.as_view(),name="addjob"),
    path('deletejob/<int:pk>',views.DeleteJob.as_view(),name="job-del"),
    path('jobview/<int:pk>',views.JobDetail.as_view(),name="jobview"),
    path('joblist',views.JobList.as_view(),name="joblist"),
    path('jobedit/<int:pk>',views.JobUpdate.as_view(),name="edit"),
    path('viewappliedjobs',views.View_appliedjobs.as_view(),name="viewjobs"),
    
]
