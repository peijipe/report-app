from django.shortcuts import render, redirect
from .models import Report
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
# from .forms import ReportForm　# ModelFormのケース
from .forms import RepoForm

def index(request):
    users = User.objects.all()
    return render(request, 'weekly_report/index.html', {'users': users})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    reports = user.report_set.all().order_by('-start_date')
    return render(request, 'weekly_report/users_detail.html', {'user': user, 'reports': reports})

# ModelFormのケース
# def reports_new(request):
#     if request.method == "POST":
#         form = ReportForm(request.POST)
#         if form.is_valid():
#             report = form.save(commit=False)
#             report.user = request.user
#             report.save()
#             messages.success(request, "報告書を提出しました")
#         return redirect('weekly_report:users_detail', pk=request.user.pk)
#     else:
#         form = ReportForm()
#     return render(request, 'weekly_report/reports_new.html', {'form': form})

def reports_new(request):
    form = RepoForm(request.POST or None)

    if form.is_valid():
        report = Report()
        report.user = request.user
        report.start_date = form.cleaned_data['start_date']
        report.end_date = form.cleaned_data['end_date']
        report.pj_name = form.cleaned_data['pj_name']
        report.outline = form.cleaned_data['outline']
        report.good_point = form.cleaned_data['good_point']
        report.bad_point = form.cleaned_data['bad_point']
        report.problem_outline = form.cleaned_data['problem_outline']
        report.weekly_project_working_hours = form.cleaned_data['weekly_project_working_hours']
        report.total_project_working_hours = form.cleaned_data['total_project_working_hours']
        report.weekly_project_overtime_hours = form.cleaned_data['weekly_project_overtime_hours']
        report.total_project_overtime_hours = form.cleaned_data['total_project_overtime_hours']
        report.weekly_internal_working_hours = form.cleaned_data['weekly_internal_working_hours']
        report.total_internal_working_hours = form.cleaned_data['total_internal_working_hours']
        report.pointed_matter = form.cleaned_data['pointed_matter']
        report.free_text = form.cleaned_data['free_text']
    
        Report.objects.create(
            user=report.user,
            start_date=report.start_date,
            end_date=report.end_date,
            pj_name=report.pj_name,
            outline=report.outline,
            good_point=report.good_point,
            bad_point=report.bad_point,
            problem_outline=report.problem_outline,
            weekly_project_working_hours=report.weekly_project_working_hours,
            total_project_working_hours=report.total_project_working_hours,
            weekly_project_overtime_hours=report.weekly_project_overtime_hours,
            total_project_overtime_hours=report.total_project_overtime_hours,
            weekly_internal_working_hours=report.weekly_internal_working_hours,
            total_internal_working_hours=report.total_internal_working_hours,
            pointed_matter=report.pointed_matter,
            free_text=report.free_text,
        )
        messages.success(request, "報告書を提出しました")
        
        return redirect('weekly_report:users_detail', request.user.id)

    return render(request, 'weekly_report/reports_new.html', {'form': form})


def reports_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'weekly_report/reports_detail.html', {'report': report})

@require_POST
def reports_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    return redirect('weekly_report:users_detail', request.user.id)

# ModelFormのケース
# def reports_edit(request, pk):
#     report = get_object_or_404(Report, pk=pk)
#     if request.method == "POST":
#         form = ReportForm(request.POST, instance=report)
#         if form.is_valid():
#             form.save()
#             return redirect('weekly_report:index')
#     else:
#         form = ReportForm(instance=report)
#     return render(request, 'weekly_report/reports_edit.html', {'form': form, 'report': report})

def reports_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == "POST":
        form = RepoForm(request.POST)
        if form.is_valid():
            report = Report()
            report.start_date = form.cleaned_data['start_date']
            report.end_date = form.cleaned_data['end_date']
            report.pj_name = form.cleaned_data['pj_name']
            report.outline = form.cleaned_data['outline']
            report.good_point = form.cleaned_data['good_point']
            report.bad_point = form.cleaned_data['bad_point']
            report.problem_outline = form.cleaned_data['problem_outline']
            report.weekly_project_working_hours = form.cleaned_data['weekly_project_working_hours']
            report.total_project_working_hours = form.cleaned_data['total_project_working_hours']
            report.weekly_project_overtime_hours = form.cleaned_data['weekly_project_overtime_hours']
            report.total_project_overtime_hours = form.cleaned_data['total_project_overtime_hours']
            report.weekly_internal_working_hours = form.cleaned_data['weekly_internal_working_hours']
            report.total_internal_working_hours = form.cleaned_data['total_internal_working_hours']
            report.pointed_matter = form.cleaned_data['pointed_matter']
            report.free_text = form.cleaned_data['free_text']

            Report.objects.filter(pk=pk).update(
                start_date=report.start_date,
                end_date=report.end_date,
                pj_name=report.pj_name,
                outline=report.outline,
                good_point=report.good_point,
                bad_point=report.bad_point,
                problem_outline=report.problem_outline,
                weekly_project_working_hours=report.weekly_project_working_hours,
                total_project_working_hours=report.total_project_working_hours,
                weekly_project_overtime_hours=report.weekly_project_overtime_hours,
                total_project_overtime_hours=report.total_project_overtime_hours,
                weekly_internal_working_hours=report.weekly_internal_working_hours,
                total_internal_working_hours=report.total_internal_working_hours,
                pointed_matter=report.pointed_matter,
                free_text=report.free_text
            )

            report = get_object_or_404(Report, pk=pk)
            return render(request, 'weekly_report/reports_detail.html', {'report': report, 'pk': pk})
    else:
        data = {
            'start_date': report.start_date,
            'end_date': report.end_date,
            'pj_name': report.pj_name,
            'outline': report.outline,
            'good_point': report.good_point,
            'bad_point': report.bad_point,
            'problem_outline': report.problem_outline,
            'weekly_project_working_hours': report.weekly_project_working_hours,
            'total_project_working_hours': report.total_project_working_hours,
            'weekly_project_overtime_hours': report.weekly_project_overtime_hours,
            'total_project_overtime_hours': report.total_project_overtime_hours,
            'weekly_internal_working_hours': report.weekly_internal_working_hours,
            'total_internal_working_hours': report.total_internal_working_hours,
            'pointed_matter': report.pointed_matter,
            'free_text': report.free_text,
        }
        form = RepoForm(data)
        
    return render(request, 'weekly_report/reports_edit.html', {'form': form, 'report': report})
