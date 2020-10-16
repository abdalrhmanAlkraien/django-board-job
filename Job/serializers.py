from rest_framework import serializers
from .models import job

class jobserializers(serializers.ModelSerializer):
    class Meta:
        model=job
        fields='__all__'
        #exclude=('slug',)
        #['title','job_type','decription','published_at','vacancy','salary']