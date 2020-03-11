from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('BME280/', views.BME280, name='BME280'),
    path('api/data/', views.get_data, name='api-data'),
    path('ajax/',views.get_day_data ,name='date'),
    path('realtime/',views.realtime ,name='realtime'),


]