from django.urls import path
from . import views

app_name = 'weekly_report'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
    path('reports/new/', views.reports_new, name='reports_new'),
    path('reports/<int:pk>/', views.reports_detail, name='reports_detail'),
    path('reports/<int:pk>/delete/', views.reports_delete, name='reports_delete'),
]