from django.db import models

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
    img=models.ImageField(upload_to=image_upload)
    categore=models.ForeignKey(Categore,on_delete=models.CASCADE)
    def __str__(self):
        return self.title




    