from .models import job
from .serializers import jobserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    job_list=job.objects.all()
    data=jobserializers(job_list,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_details_api(request,id):
    job_det=job.objects.get(id=id)
    data=jobserializers(job_det).data
    return Response({'data':data})

class Job_List_Api(generics.ListAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializers