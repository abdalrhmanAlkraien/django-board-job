from django.shortcuts import render,redirect,reverse
from .forms import SignUpForm ,Userform,Profilform
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
        print("done 1")
        prof=profile.objects.get(user=request.user)
        print("done 2")
        return render(request,'accounts/profile.html',{'profile':prof})
    else:
        return redirect('login')
    

def edit_profile(request):
    if  request.user.is_authenticated:
        prof=profile.objects.get(user=request.user)
        if request.method=="POST":
            
            profileform=Profilform(request.POST,request.FILES,instance=prof)
            userform=Userform(request.POST,instance=request.user)
            if profileform.is_valid() and userform.is_valid():
                userform.save()
                profileform.save(commit=False)
                profileform.user=request.user
                profileform.save()
                return redirect(reverse('accounts:profile'))
        else:
            profileform=Profilform(instance=prof)
            userform=Userform(instance=request.user)
        context={'profileform':profileform,'userform':userform}
        return render(request,'accounts/edit_profile.html',context)

    else:
        return redirect('login')
        


