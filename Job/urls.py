from django.urls import path,include
from . import views
from . import api

app_name='Job'
urlpatterns = [
    path('',views.job_list,name="list_job"),
    path('jobadd',views.add_job,name="add_job"),
    path('<str:slug>',views.job_details,name="job_details"),
    #api
    path('api/job',api.job_list_api,name="job_list_api"),
    path('api/job/<int:id>',api.job_details_api,name="details"),

    #CBV API
    path('api/v2/job/',api.Job_List_Api.as_view(),name="list")
    
]