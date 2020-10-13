from django.shortcuts import render,get_object_or_404,redirect
from .models import job
from django.core.paginator import Paginator
from .forms import Applyform,addjob
from django.contrib.auth import user_logged_in
from django.urls import reverse

def job_list(request):
    jobs=job.objects.all()
    paginator = Paginator(jobs, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'job\job_list.html',context)

def job_details(request,slug):
    jobs=job.objects.get(slug=slug)
    if request.method=='POST':
        form=Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=jobs
            print("done")
            myform.save()
    else:
        form=Applyform()

    context={'jobs':jobs,'form':form}
    return render(request,'job\job_detalis.html',context)

def add_job(request):
    if request.method=="POST":
        form=addjob(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            print("ok!!!!!!")
            return redirect(reverse("Job:list_job"))
    else:
        form=addjob()
    context={'form':form}
    return render(request,'job/jobadd.html',context)