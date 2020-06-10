from django.contrib.admin.filters import (
    SimpleListFilter,
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter
)
import os 




class SimpleDropdownFilter(SimpleListFilter):
    template = 'templates/dropdown_filter.html'



class DropdownFilter(AllValuesFieldListFilter):
    template = os.getcwd() + '/project_track/templates/dropdown_filter.html'
#What is the link

class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'templates/dropdown_filter.html'


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'templates/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'templates/dropdown_filter.html'
