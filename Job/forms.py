from django import forms
from .models import Apply,job

class Applyform(forms.ModelForm):
    class Meta:
        model=Apply
        fields =['name','email','website','cv','converletter']

class addjob(forms.ModelForm):
    class Meta:
        model=job
        fields="__all__"
        exclude=('slug','owner')