from django.contrib import admin
from .models import Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pj_name', 'start_date', 'end_date', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'user')

admin.site.register(Report, ReportAdmin)

