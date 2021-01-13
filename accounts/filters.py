import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Дата от')
	end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='Дата до')
	note = CharFilter(field_name='note', lookup_expr='icontains', label='По ключевым словам')
	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']
		
