from django.shortcuts import render,redirect
from .forms import SignUpForm 
from django.contrib.auth import authenticate,login
from .models import profile
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
        
            
    else:
        form=SignUpForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)

def profile_view(request):
    if request.user.is_authenticated:
        #if Profile.objects.filter(user=request.user).exists():
         prof=profile.objects.get(user=request.user)
         return render(request,'accounts/profile.html',{'profile':prof})
    else:
        return redirect('login')
    

def edit_profile(request):
    pass


