from django.contrib import admin

from admin_tools.models import Department, Employee


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
