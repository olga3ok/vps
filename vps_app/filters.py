import django_filters
from .models import VPS


class VPSFilter(django_filters.FilterSet):
    class Meta:
        model = VPS
        fields = {
            'uid': ['exact', 'icontains'],
            'cpu': ['exact', 'gte', 'lte'],
            'ram': ['exact', 'gte', 'lte'],
            'hdd': ['exact', 'gte', 'lte'],
            'status': ['exact'],
        }