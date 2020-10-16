from django.db import models

# Create your models here.
class information(models.Model):
    location=models.CharField(max_length=100)
    mobile=models.CharField(max_length=14)
    email=models.EmailField(max_length=100)
    def __str__(self):
        return str(self.email)


    
