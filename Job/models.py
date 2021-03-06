from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
JOB_TYPE = (
            ('Full Time',"Full Time"),
            ("Part Time","Part Time")
          )
class Categore(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

def image_upload(instance,filename):
    name,exe=filename.split('.')
    return "jobs/%s.%s"%(instance.id,exe)
    


class job (models.Model):
    title=models.CharField(max_length=50)
    #location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    decription=models.TextField(max_length=500,default=None,null=True)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=0)
    img=models.ImageField(upload_to='')
    categore=models.ForeignKey(Categore,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,related_name="job_user",on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(job,self).save(*args,**kwargs)
    def __str__(self):
        return self.title

class Apply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    website=models.URLField()
    cv=models.FileField(upload_to='apply/')
    converletter=models.TextField()
    job=models.ForeignKey(job, related_name="apply_job", on_delete=models.CASCADE)
    Apply_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    