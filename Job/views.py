from django.shortcuts import render,get_object_or_404
from .models import job

def job_list(request):
    jobs=job.objects.all()
    context={'jobs':jobs}
    return render(request,'job\job_list.html',context)

def job_details(request,id):
    jobs=job.objects.get(id=id)
    context={'jobs':jobs}
    return render(request,'job\job_detalis.html',context)