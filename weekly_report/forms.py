from django.forms import ModelForm
from .models import Report

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['start_date', 'end_date', 'pj_name', 'outline', 'good_point', \
            'bad_point', 'problem_outline', 'weekly_project_working_hours', \
            'total_project_working_hours', 'weekly_project_overtime_hours', \
            'total_project_overtime_hours', 'weekly_internal_working_hours', \
            'total_internal_working_hours', 'pointed_matter', 'free_text']