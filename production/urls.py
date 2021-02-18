from django.urls import path
from . import views

app_name = 'production'

urlpatterns = [

    path('', views.production, name = 'production'),
    #REPORT
    path('report/', views.report_shift, name = 'report'),
    path('report/<int:n_shift>/', views.report_view, name = 'report_shift'),
    path('report/list/', views.report_list, name = 'report_list'),
    #HOLIDAY REQUEST
    path('holiday_request/',views.holiday_request, name = 'holiday_request'),
    path('holiday_request/<int:request_id>/', views.h_request_pdf, name = 'h_request_pdf'),
    path('report/list/<str:day_1>/<str:day_2>/', views.report_list_pdf, name = 'report_list_pdf'),
    #TASK
    path('task_list/', views.task_list, name = 'task_list'),
    path('task_list/done/<str:pk>/', views.done_task, name = 'done_task'),
    path('task_list/delete/<str:pk>/', views.delete_task, name = 'delete_task'),
    path('done_today/', views.task_done_today, name = 'task_done_today'),
    path('done_last_week/', views.task_done_last_week, name = 'task_done_last_week'),
    #API
    path('api/', views.apioverview, name = 'api_view'),
    path('api/report-list/', views.reports_api, name = 'api_reports'),
    path('api/report-list/<str:pk>/', views.single_report_api, name = 'single_api_report'),
    path('api/report-list-json/', views.reports_api_json, name = 'api_reports_json'),
    path('api/report-list-json/<str:pk>/', views.single_report_api_json, name  =  'single_api_report_json'),
            ]
