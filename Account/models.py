from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=30)

class profile(models.Model):
    user=models.OneToOneField(User,  on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10)
    image=models.ImageField(upload_to="profile/")
    city=models.ForeignKey(City,related_name="prfoile_city",on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)


