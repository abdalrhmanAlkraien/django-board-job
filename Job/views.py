from django.shortcuts import render,get_object_or_404
from .models import job
from django.core.paginator import Paginator

def job_list(request):
    jobs=job.objects.all()
    paginator = Paginator(jobs, 1) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'job\job_list.html',context)

def job_details(request,slug):
    jobs=job.objects.get(slug=slug)
    context={'jobs':jobs}
    return render(request,'job\job_detalis.html',context)