from django.contrib import admin

# local apps
from .models import Employee, Faculty, Department, UserType, Designation
# Register your models here.

admin.site.register(Employee)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(UserType)
admin.site.register(Designation)
