import django_filters
from .models import *

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = StudentEmployee
        fields = '__all__'
        exclude = ['byu_id', 'emp_first', 'emp_last','email','phone']

class SupervisorFilter(django_filters.FilterSet):
    class Meta:
        model = Supervisor
        fields = '__all__'
        exclude = ['supervisor_id']

class WorkFilter(django_filters.FilterSet):
    class Meta:
        model = StudentWork
        fields = '__all__'