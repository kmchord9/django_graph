from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TempData
import datetime
#import pytz
from django.utils import timezone

# Create your views here.


def index(request):
    return render(request, 'test.html')

def BME280(request):
    return render(request, 'BME280.html')

def realtime(request):
    return render(request, 'realtime.html')


def get_data(request):
    #GETリクエストの場合には送られた年月日のデータ
    if "prm" in request.GET:
            data = request.GET.get('prm').split('-')
            y = data[0]
            m = data[1]
            d = data[2]
            title = '{}/{}/{}'.format(y,m,d)
    #GETリクエスト出ない場合には今日の日付
    else:
            dt_now = datetime.datetime.now()
            y = dt_now.year
            m = dt_now.month
            d = dt_now.day
            title = dt_now.strftime("%Y/%m/%d")

    #上記の日付データに基づいてクエリを作成してデータ取得
    #クエリで得られるタイムゾーンはずれるのでtimezone関数により修正
    data = {
        "title": title,
        "labels": [timezone.localtime(d.date).strftime("%H:%M:%S") for d in TempData.objects.filter(date__year=y, date__month=m, date__day=d)],
        "temp":[d.temp for d in TempData.objects.filter(date__year=y, date__month=m, date__day=d)],
        }

    return JsonResponse(data)
    
def get_day_data(request):
    #d = {'date': request.GET.get('date')}
    data = request.GET.get('date').split('-')
    y = data[0]
    m = data[1]
    d = data[2]
    return HttpResponse(y+m+d)
