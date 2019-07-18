from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    pj_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    outline = models.TextField()
    good_point = models.TextField(blank=True)
    bad_point = models.TextField(blank=True)
    problem_outline = models.TextField(blank=True)

    weekly_project_working_hours = models.FloatField()
    total_project_working_hours = models.FloatField()

    weekly_project_overtime_hours = models.FloatField()
    total_project_overtime_hours = models.FloatField()

    weekly_internal_working_hours = models.FloatField()
    total_internal_working_hours = models.FloatField()

    pointed_matter = models.TextField(blank=True)
    free_text = models.TextField(blank=True)

    def __str__(self):
        return self.pj_name

    