from django.urls import path
from jobseeker import views


urlpatterns = [
    path('register/',views.Register.as_view(),name='reg'),
    # path('signin/',views.Signin.as_view(),name='login'),
    path('seekerindex/',views.Student_home.as_view(),name='seekerindex'),
    path('seekerprofile/',views.Profile.as_view(),name='seekerprofile'),
    path('profileview/<int:pk>',views.ProfileView.as_view(),name='profileview'),
    path('profileedit/<int:pk>',views.UpdateProfile.as_view(),name='profileedit'),
    path('signout/',views.signout.as_view(),name='signout'),
    path('detail/<int:pk>',views.JobDetailview.as_view(),name='jobdetail'),
    path('applyjob/<int:pk>',views.ApplyJobview.as_view(),name='applyjob'),
    path('applied',views.Applied_jobs.as_view(),name='appliedjobs'),
    path('deletejob/<int:pk>',views.Delete_job.as_view(),name='delete_job'),
]