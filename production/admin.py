from django.contrib import admin
from .models import Report, Holiday_request, Task, Info

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display =('shift','team','created','product_A','product_B','description') 
    list_filter = ['shift', 'team','created']
    list_editable = ['product_A','product_B']

@admin.register(Holiday_request)
class Holiday_requestAdmin(admin.ModelAdmin):
    list_display = ('first_name','surname','email','department','date_begin','date_end','notice','approved')
    list_filter = ('first_name','surname','email',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    class Meta:
        models = Task
        fields = '__all__'

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    class Meta:
        models = Info
        fields = '__all__'