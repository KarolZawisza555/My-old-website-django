from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField 


TODAY = timezone.now().date()
DEPARTMENTS = ((1,'Electrical'),(2,'IT'),(3,'Bookkeeping'),(4,'Production'))
LIST_SHIFT = (('1','Shift_1'),('2','Shift_2'),('3','Shift_3'))
LIST_TEAM = (('1','Team_1'),('2','Team_2'),('3','Team_3'),('4','Team_4'))
LIST_QUANITY =[(i, str(i)) for i in range(0, 21)]


class Report(models.Model):

    shift = models.CharField(choices = LIST_SHIFT, max_length=10,unique_for_date = 'created')
    team = models.CharField(choices = LIST_TEAM, max_length = 10, default = '1')
    product_A = models.PositiveIntegerField(default = 0, choices = LIST_QUANITY)
    product_B = models.PositiveIntegerField(default = 0, choices = LIST_QUANITY)
    description = models.TextField(max_length = 500, blank = False, null = False)
    created = models.DateField(default = timezone.now,db_index= True) 

    class Meta:
        ordering =('created','-shift')
    
    def __str__(self):
        return '{} {} {}'.format(self.shift, self.team, self.created)

class Holiday_request(models.Model):

    first_name = models.CharField(max_length = 20,blank = False, null = False)
    surname = models.CharField(max_length = 20,blank = False, null = False)
    email = models.EmailField(blank = False, null = False)
    department = models.PositiveIntegerField(choices = DEPARTMENTS, blank = False, null = False)
    date_begin = models.DateField(default = TODAY)
    date_end = models.DateField(default = TODAY)
    notice = RichTextField(max_length = 500,blank = False, null = False)
    created = models.DateField(auto_now_add = True)
    approved = models.BooleanField(default = False)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return  " {} {}  from {} to {} ".format(self.first_name, self.surname, self.date_begin, self.date_end)


class Task(models.Model):
    title = models.CharField(max_length = 150)
    done = models.BooleanField(default = False)
    created = models.DateField(auto_now_add = True,db_index=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

class Info(models.Model):
    title = models.CharField(max_length=25)
    created = models.DateField(auto_now_add=True,db_index=True)
    time = models.TimeField(auto_now_add = True)

    def __str__(self):
        return "{} {} {}".format(self.created, self.time, self.title)
