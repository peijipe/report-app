from django.shortcuts import render, redirect
from .models import Report
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import ReportForm

def index(request):
    reports = Report.objects.all().order_by('-start_date')
    return render(request, 'weekly_report/index.html', {'reports': reports})

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    reports = user.report_set.all().order_by('-start_date')
    return render(request, 'weekly_report/users_detail.html', {'user': user, 'reports': reports})

def reports_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, "報告書を提出しました")
        return redirect('weekly_report:users_detail', pk=request.user.pk)
    else:
        form = ReportForm()
    return render(request, 'weekly_report/reports_new.html', {'form': form})

def reports_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'weekly_report/reports_detail.html', {'report': report})

@require_POST
def reports_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    return redirect('weekly_report:users_detail', request.user.id)

def reports_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('weekly_report:index')
    else:
        form = ReportForm(instance=report)
    return render(request, 'weekly_report/reports_edit.html', {'form': form, 'report': report})
