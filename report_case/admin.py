from django.contrib import admin
from .models import NewCase
# Register your models here.

@admin.register(NewCase)
class CaseAdmin(admin.ModelAdmin):
    list_display=[
        'case_code','age','gender','date','outcome','test_status','location','additional_information'
    ]
