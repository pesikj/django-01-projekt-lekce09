import django_filters
from crm.models import Opportunity

class OpportunityFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name ="company__name", lookup_expr='icontains')

    class Meta:
        model = Opportunity
        fields = ['company', 'sales_manager', "status"]
