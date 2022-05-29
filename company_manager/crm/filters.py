import django_filters
from crm.models import Company, Opportunity


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

class OpportunityFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
            Div(
                Div("company", css_class="col-sm-3"),
                Div("sales_manager", css_class="col-sm-3"),
                Div("status", css_class="col-sm-2"),
                Submit('submit', 'Filter', css_class='button'),
                css_class="row"
            )
        )

class OpportunityFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(field_name ="company__name", lookup_expr='icontains')

    class Meta:
        model = Opportunity
        fields = ['company', 'sales_manager', "status"]

class CompanyFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
            Div(
                Div("status", css_class="col-sm-3"),
                Div("name", css_class="col-sm-3"),
                Div("identification_number", css_class="col-sm-2"),
                Submit('submit', 'Filter', css_class='button'),
                css_class="row"
            )
        )

class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name ="name", lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['status', 'name', "identification_number"]
