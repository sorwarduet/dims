from django.contrib import admin
from django.contrib.admin.models import LogEntry
# local apps
from .models import Employee, Faculty, Department, UserType, Designation
# Register your models here.

admin.site.register(Employee)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(UserType)
admin.site.register(Designation)



@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]