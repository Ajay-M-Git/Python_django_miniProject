from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    list_filter=('company')
    
admin.site.register(Company)
admin.site.register(Employee)
