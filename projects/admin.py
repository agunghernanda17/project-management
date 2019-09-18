from adminfilters.multiselect import UnionFieldListFilter
from advanced_filters.admin import AdminAdvancedFiltersMixin
from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.translation import ugettext_lazy as _
from .models import Task
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter


class TaskAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('number', 'project_title', 'user', 'vendor', 'created_at','target_implement_date','actual_implement_date', 'blueprint_title', 'priority', 'state')
    list_display_links = ('number', 'project_title')
    search_fields = ('id', 'project_title', 'status__item_description',
                     'user__username', 'user__first_name', 'user__last_name',
                     'vendor__name', 'vendor__email')
    list_filter = (
        ('user', RelatedDropdownFilter),
        ('vendor', RelatedDropdownFilter),
        ('state', UnionFieldListFilter),
        ('priority', UnionFieldListFilter),
        'target_implement_date'
    )
    advanced_filter_fields = (
        'user__username',
        'vendor__name',
        'state',
        'priority',
        'target_implement_date',
        'created_at',
        'created_by',
        'project_title',
    )
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'last_modified', 'created_by')
    autocomplete_fields = ['user', 'vendor']

    fieldsets = (               # Edition form
        (None,                   {'fields': (('project_title', 'project_owner'), 'user', 'vendor', 'blueprint_title', 'blueprint',
                                            'changes', 'release','register_date', ('target_implement_date', 'actual_implement_date'),
                                             ('state', 'priority'), 'mandays', 'remarks', 'references')}),
        (_('More...'), {'fields': (('created_at', 'last_modified'), 'created_by'), 'classes': ('collapse',)}),
    )
  

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 32})
        }
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': (('project_title','project_owner'), 'user', 'vendor', 'blueprint_title', 'blueprint', 
                                            'changes', 'release','register_date', ('target_implement_date', 'actual_implement_date'),
                                             ('state', 'priority'), 'mandays', 'remarks', 'references')}),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)
