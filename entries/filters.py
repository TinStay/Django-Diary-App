import django_filters
from django_filters import DateFilter, CharFilter
from .models import Entry

class EntryFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_posted', lookup_expr='gte')
    # end_date = DateFilter(field_name='date_posted', lookup_expr='lte')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    # text = CharFilter(field_name='text', lookup_expr='icontains')

    class Meta:
        model = Entry
        fields = '__all__'
        exclude =["author",'date_posted','text']