import django_filters
from .models import Profile, profile
class Profilefilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields =['ssn']