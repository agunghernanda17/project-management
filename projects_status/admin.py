from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Projects_status
#from .models import Charts
from django.db.models import Count, Sum, Min, Max, DateTimeField

# @admin.register(Charts)
# class ChartsAdmin(admin.ModelAdmin):
#     change_list_template = 'charts_admin.html'
#     date_hierarchy = 'created_at'
#     list_display = ('id', 'task','user','project_owner', 'user_requirements','development','sit','uat','implementation')
    
class Projects_statusAdmin(admin.ModelAdmin):
    list_display = ('id', 'task','user','project_owner', 'user_requirements','development','sit','uat','implementation','is_done')
    list_display_links = ('task','user')
    #search_fields = ('id','comment')
    change_list_template = 'charts_admin.html'
    list_filter = ('user','project_owner','is_done')
    ordering = ('task',)
    readonly_fields = ('created_at', 'last_modified', 'created_by')
    fieldsets = (  # Edition form
        (None, {'fields': ('task','user','comment','project_owner',('user_requirements','user_comment'),('development','dev_comment'),
		('sit','sit_comment'),('uat','uat_comment'),('implementation','imp_comment'),'is_done')}),
        (_('More...'), {'fields': (('created_at', 'last_modified'), 'created_by'), 'classes': ('collapse',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': ('task','user','comment','project_owner',('user_requirements','user_comment'),('development','dev_comment'),
		('sit','sit_comment'),('uat','uat_comment'),('implementation','imp_comment'),'is_done')}),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Projects_status, Projects_statusAdmin)
