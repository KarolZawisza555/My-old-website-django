from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.urls import reverse
from .models import Report, Holiday_request, Task, Info
from .forms import ReportForm, DayForm, HolidayForm, TaskForm
from datetime import date
from datetime import timedelta
from django.db.models import Sum
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReportSerializer


TODAY = timezone.now().date()
WEEK = timezone.timedelta(days=7)
WEEK_AGO = TODAY - WEEK



def report_view(request,n_shift=1):
    if n_shift not in [1,2,3]:
        return redirect(reverse('production:report_shift'))
    template = 'report.html'
    if request.method == 'POST':
        check_quantity=len(Report.objects.all().filter(created=TODAY,shift=n_shift))
        report_form = ReportForm(data = request.POST)  
        if report_form.is_valid() and check_quantity == 0:
            report=report_form.save(commit = False)
            report.shift=n_shift
            report.save()
            context={'new':True}
            return render(request,template,context)
        elif report_form.is_valid() and check_quantity == 1:
            report=get_object_or_404(Report, created=TODAY,shift=n_shift)
            report.delete()
            report=report_form.save(commit = False)
            report.shift=n_shift
            report.save()
            context={'updated':True}
            return render(request,template,context)
    else:
        report_form = ReportForm()
    context = {'report_form':report_form,'n_shift':n_shift}
    Info.objects.create(title='report_view')
    return render(request,template,context)

def report_shift(request):
    template='report_shift.html'
    context={}
    Info.objects.create(title='report_shift')
    return render(request,template,context)


def report_list(request):
    if request.method=='POST':
        form=DayForm(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            try:
                day1, day2 = cd['day_1'],cd['day_2']
                report_list = Report.objects.all().filter(created__gte=day1,created__lte=day2)
                number_of_records=len(report_list)
            except:
                return redirect(reverse('production:report_list'))
        else:
            return redirect(reverse('production:report_list'))
    else:   
        day1, day2 = WEEK_AGO,TODAY
        report_list=Report.objects.all().filter(created__gte=day1, created__lte=day2)
        number_of_records = len(report_list) 
    sum_product_A = report_list.aggregate(Sum('product_A'))
    sum_A = sum_product_A['product_A__sum']
    sum_product_B = report_list.aggregate(Sum('product_B'))
    sum_B = sum_product_B['product_B__sum']
    template = 'report_list.html'
    context = {'report_list':report_list,
                'form':DayForm,
                'number_of_records':number_of_records,
                'sum_A':sum_A,'sum_B':sum_B,
                'day_1':day1,'day_2':day2}
    Info.objects.create(title='report_list')
    return render(request,template, context)


def holiday_request(request):
    if request.method == 'POST':
        forms = HolidayForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            number_request = Holiday_request.objects.latest('id')           
            context = { 'forms': forms,'POST':'POST','number_id':number_request.id}        
    else:   
        forms = HolidayForm()
        context = { 'forms': forms }
    template = 'Holiday_request.html'
    Info.objects.create(title='holiday_request')
    return render(request,template,context)

def production(request):
    template = "production.html"
    context = {}
    return render(request,template,context)


def h_request_pdf(request, request_id):
    h_request = get_object_or_404(Holiday_request, id=request_id)
    html = render_to_string('pdf_dir/template_pdf.html',{'h_request': h_request})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="h_request_{}.pdf"'.format(h_request.id)
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.PDF_CSS)])
    Info.objects.create(title='h_request_pdf')
    return response


def report_list_pdf(request, day_1,day_2):
    report_list = Report.objects.all().filter(created__gte=day_1,created__lte=day_2)
    sum_product_A = report_list.aggregate(Sum('product_A'))
    sum_A = sum_product_A['product_A__sum']
    sum_product_B = report_list.aggregate(Sum('product_B'))
    sum_B = sum_product_B['product_B__sum']
    context = {'report_list': report_list,
                'sum_product_A':sum_A,
                'sum_product_B':sum_B,
                'number_of_records':len(report_list) }
    html = render_to_string('pdf_dir/template_pdf_table.html',context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report_list.pdf"'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.PDF_CSS)])
    Info.objects.create(title='report_list_pdf')
    return response


def task_list(request):
    template = 'task_list.html'
    task_list = Task.objects.filter(done=False,created=TODAY)
    if request.method == "POST":
        task_form = TaskForm(data = request.POST)
        if task_form.is_valid():
            cd = task_form.cleaned_data
            Task.objects.create(title=cd['title'])
    else:
        task_form = TaskForm()
    context = {'task_list': task_list, 'task_form':task_form}
    Info.objects.create(title='task_list')
    return render(request, template, context)

def done_task(request,pk):
    task = get_object_or_404(Task, id=pk)
    task.done = True
    task.save()
    Info.objects.create(title='done_task')
    return redirect("production:task_list")

def delete_task(request,pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    Info.objects.create(title='delete_task')
    return redirect("production:task_list")

def task_done_today(request):
    template = 'task_list_done.html'
    task_list = Task.objects.filter(done=True, created=TODAY)
    context = {'task_list': task_list,'TODAY':TODAY}
    Info.objects.create(title='task_done_today')
    return render(request, template, context)

def task_done_last_week(request):
    template = 'task_list_done.html'
    task_list = Task.objects.filter(done=True, created__gte=WEEK_AGO, created__lte=TODAY)
    context = {'task_list': task_list,}
    Info.objects.create(title='task_done_last_week')
    return render(request, template, context)

@api_view(['GET'])
def apioverview(request):
    word="data"
    return Response(word)


@api_view(['GET'])
def reports_api(request):
    reports = Report.objects.all()[:50]
    serializers = ReportSerializer(reports, many=True )
    return Response(serializers.data)

@api_view(['GET'])
def single_report_api(request,pk):
    reports = Report.objects.get(id=pk)
    serializers = ReportSerializer(reports, many=False)
    return Response(serializers.data)

@api_view(['GET'])
def reports_api_json(request):
    reports = Report.objects.all()[:50]
    serializers = ReportSerializer(reports, many=True )
    return JsonResponse(serializers.data)

@api_view(['GET'])
def single_report_api_json(request,pk):
    reports = Report.objects.get(id=pk)
    serializers = ReportSerializer(reports, many=False)
    return JsonResponse(serializers.data)




