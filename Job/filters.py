import django_filters
from .models import job

class jobFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = job
        fields = '__all__'
        exclude=['published_at','vacancy','salary','img','slug','owner','decription']