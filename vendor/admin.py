from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','pic_name', 'email', 'phones', 'address', 'is_company')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email')

    list_filter = ('is_company',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'last_modified', 'created_by')
    fieldsets = (  # Edition form
        (None, {'fields': (('name', 'is_company'), ('pic_name', 'email'), ('phone', 'mobile'), ('address',), ('comment',))}),
        (_('More...'), {'fields': (('created_at', 'last_modified'), 'created_by'), 'classes': ('collapse',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': (('name', 'is_company'), ('pic_name', 'email'), ('phone', 'mobile'), ('address',), ('comment',))}),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Vendor, VendorAdmin)
