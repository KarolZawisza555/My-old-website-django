import datetime
from .models import Report
import random

text=['OK','Good','Perfectly','Faultlessly','Poorly']
quantity =[i for i in range(0, 21)]
start = datetime.date(2019,1,1)
next = datetime.timedelta(1)
for x in range(772):
    team = [1,2,3,4]
    for i in (1,2,3):
        team_selected = random.choice(team)
        team.remove(team_selected)
        Report.objects.create(shift = i,team = team_selected,product_A = random.choice(quantity),product_B = random.choice(quantity),created = start+datetime.timedelta(x),description = random.choice(text))


    
        