from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Aplikasi


class AplikasiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'project_owner','vendor')
    list_display_links = ('id', 'name', 'project_owner')
    search_fields = ('id', 'name', 'project_owner')

    list_filter = ('project_owner',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'last_modified', 'created_by')
    fieldsets = (  # Edition form
        (None, {'fields': ('name','project_owner', 'vendor', ('comment'))}),
        (_('More...'), {'fields': (('created_at', 'last_modified'), 'created_by'), 'classes': ('collapse',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': ('name','project_owner', 'vendor', ('comment'))}),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Aplikasi, AplikasiAdmin)
