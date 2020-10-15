from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name='accounts'
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('profile',views.profile_view,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile')
    
]