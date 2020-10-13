from django.urls import path,include
from . import views

app_name='Job'
urlpatterns = [
    path('',views.job_list,name="list_job"),
    path('jobadd',views.add_job,name="add_job"),
    path('<str:slug>',views.job_details,name="job_details"),
    
]