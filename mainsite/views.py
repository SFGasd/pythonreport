from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import PlayList, TaipeiStationExtraData, TaipeiStationInOut
from mainsite.models import AccessInfo
import random
from datetime import datetime

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    return render(request,"index.html", locals())

def taipei(request):
    return render(request,"taipei.html", locals())
def taipeicar(request):
    return render(request,"taipeicar.html", locals())
def playlist(request):
    now = datetime.now()
    items = PlayList.objects.all()
    return render(request, "playlist.html", locals())

def taipeistationchart(request, sta_num = 0):
    tp_sta_data = TaipeiStationInOut.objects.all().order_by('year')
    station_dict = dict()
    station_name = set()
    station_year = set()
    for item in tp_sta_data:
        station_name.add(item.name)
    station_name = sorted(list(station_name))
    for count in range(len(station_name)):
        station_dict[count] = station_name[count]
    station_index = station_dict.keys()
    station_index_name = station_dict.values()
    station = TaipeiStationInOut.objects.filter(name = station_dict[sta_num]).order_by('year')
    for item in station:
        station_year.add(item.year)
    station_year = sorted(list(station_year))
    station_in = station.filter(io_class = '進站')
    station_out = station.filter(io_class = '出站')
    chart_name = station_dict[sta_num]
    return render(request, "taipeistationchart.html", locals())

def taipeistationmileagechart(request, mileage_id=0):
    tp_sta_data = TaipeiStationExtraData.objects.all()
    station_yeardate = list()
    station_mileage = list()
    station_year = dict()
    station_year[0] = '100年~108年'
    for count in range(1,10):
        station_year[count] = str(99+count) + '年'
    
    display_class = station_year[mileage_id]
    for item in tp_sta_data:
        if mileage_id == 0:
            station_yeardate.append(item.year_date)
            station_mileage.append(item.total_mileage)
        else:
            if str(station_year[mileage_id]) in item.year_date:
                station_yeardate.append(item.year_date)
                station_mileage.append(item.total_mileage)
    return render(request, "taipeistationmileagechart.html", locals())

def taipeistationpersontimeschart(request, persontimes_id=0):
    tp_sta_data = TaipeiStationExtraData.objects.all()
    station_yeardate = list()
    station_persontimes = list()
    station_year = dict()
    station_year[0] = '100年~108年'
    for count in range(1,10):
        station_year[count] = str(99+count) + '年'
    
    display_class = station_year[persontimes_id]
    for item in tp_sta_data:
        if persontimes_id == 0:
            station_yeardate.append(item.year_date)
            station_persontimes.append(item.total_persontimes)
        else:
            if str(station_year[persontimes_id]) in item.year_date:
                station_yeardate.append(item.year_date)
                station_persontimes.append(item.total_persontimes)
    return render(request, "taipeistationpersontimeschart.html", locals())

def taipeistationincomechart(request, income_id=0):
    tp_sta_data = TaipeiStationExtraData.objects.all()
    station_yeardate = list()
    station_income = list()
    station_year = dict()
    station_year[0] = '100年~108年'
    for count in range(1,10):
        station_year[count] = str(99+count) + '年'
    
    display_class = station_year[income_id]
    for item in tp_sta_data:
        if income_id == 0:
            station_yeardate.append(item.year_date)
            station_income.append(item.total_income)
        else:
            if str(station_year[income_id]) in item.year_date:
                station_yeardate.append(item.year_date)
                station_income.append(item.total_persontimes)
    return render(request, "taipeistationincomechart.html", locals())