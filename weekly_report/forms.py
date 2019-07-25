from django.forms import ModelForm
from .models import Report

# ModelFormのケース
# class ReportForm(ModelForm):
#     class Meta:
#         model = Report
#         fields = ['start_date', 'end_date', 'pj_name', 'outline', 'good_point', \
#             'bad_point', 'problem_outline', 'weekly_project_working_hours', \
#             'total_project_working_hours', 'weekly_project_overtime_hours', \
#             'total_project_overtime_hours', 'weekly_internal_working_hours', \
#             'total_internal_working_hours', 'pointed_matter', 'free_text']

from django import forms

class RepoForm(forms.Form):
    start_date = forms.DateField(
        label='開始日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    end_date = forms.DateField(
        label='終了日',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    pj_name = forms.CharField(
        label='案件名',
        max_length=50,
        required=True,
    )

    outline = forms.CharField(
        label='タスク一覧',
        required=True,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100, 'placeholder': 'タスク概要、期限、進捗'})
    )

    good_point = forms.CharField(
        label='うまくいった点',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100, 'placeholder': '概要、理由'})
    )

    bad_point = forms.CharField(
        label='うまくいかなかった点',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100, 'placeholder': '概要、理由、次の一手'})
    )

    problem_outline = forms.CharField(
        label='課題',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100, 'placeholder': '課題概要、課題解決に向けて取り組んでいること、アラートなど'})
    )

    weekly_project_working_hours = forms.IntegerField(
        label='週間稼働時間',
        required=True,
        min_value=0
    )

    total_project_working_hours = forms.IntegerField(
        label='累計稼働時間',
        required=True,
        min_value=0
    )

    def clean_total_project_working_hours(self):
        weekly_project_working_hours = self.cleaned_data['weekly_project_working_hours']
        total_project_working_hours = self.cleaned_data['total_project_working_hours']

        if total_project_working_hours < weekly_project_working_hours:
            raise forms.ValidationError('時間を見直してください。')

        return total_project_working_hours
    
    weekly_project_overtime_hours = forms.IntegerField(
        label='週間残業時間',
        required=True,
        min_value=0
    )

    total_project_overtime_hours = forms.IntegerField(
        label='累計残業時間',
        required=True,
        min_value=0
    )

    def clean_total_project_overtime_hours(self):
        weekly_project_overtime_hours = self.cleaned_data['weekly_project_overtime_hours']
        total_project_overtime_hours = self.cleaned_data['total_project_overtime_hours']

        if total_project_overtime_hours < weekly_project_overtime_hours:
            raise forms.ValidationError('時間を見直してください。')

        return total_project_overtime_hours
    
    weekly_internal_working_hours = forms.IntegerField(
        label='社内業務 週間残業時間',
        required=True,
        min_value=0
    )

    total_internal_working_hours = forms.IntegerField(
        label='社内業務 累計残業時間',
        required=True,
        min_value=0
    )

    def clean_total_internal_working_hours(self):
        weekly_internal_working_hours = self.cleaned_data['weekly_internal_working_hours']
        total_internal_working_hours = self.cleaned_data['total_internal_working_hours']

        if total_internal_working_hours < weekly_internal_working_hours:
            raise forms.ValidationError('時間を見直してください。')

        return total_internal_working_hours

    pointed_matter = forms.CharField(
        label='指摘された点',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100})
    )

    free_text = forms.CharField(
        label='自由欄',
        required=False,
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100})
    )
