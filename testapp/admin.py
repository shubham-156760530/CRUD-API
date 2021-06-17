from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal','eaddr']

admin.site.register(Employee, EmployeeAdmin)
# Register your models here.

#Performing CRUD operations

#Retrieve - R
#   1. Get a particular record based on matched id
#   2. Get all records
