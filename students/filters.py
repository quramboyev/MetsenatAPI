import django_filters
from .models import StudentModel, UniversityModel
from django.db.models import F


class StudentFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    university = django_filters.CharFilter(field_name='university')
    type = django_filters.CharFilter(field_name='type')
    
    paid_percent = django_filters.NumberFilter(method='filter_paid_percent', label='Процент оплаты >= X')

    class Meta:
        model = StudentModel
        fields = ['full_name', 'university', 'type']

    def filter_paid_percent(self, queryset, name, value):
        return queryset.annotate(
            percent_paid=100 * (F('allocated_amount') / F('contract_amount'))
        ).filter(percent_paid__gte=value)


class UniversityFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = UniversityModel
        fields = ['name']
        ordering = ['name']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.queryset = self.queryset.filter(students__isnull=False).distinct()