import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mychart.settings')
import sys
import random
import django
django.setup()
from chart.models import TempData
from time import sleep

for i in range(50):

    T = random.uniform(20,30)
    create_data = TempData(temp=T)
    create_data.save()
    sleep(1)
    print("{}回目記録しました".format(i))



