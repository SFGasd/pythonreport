import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from mainsite.models import TaipeiStationInOut
with open('taipeistationio.csv', newline='', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    datas = list(rows)[:19]

station_data = list()
inconnect_year = list()
for station in range(2,109):
    for row in datas:
        inconnect_year.append(row[0])
        station_data.append(row[station])
    station_name = station_data[0]
    station_in = list(station_data)[1:19:2]
    station_out = list(station_data)[2:19:2]
    station_year = list(inconnect_year)[1:19:2]
    for i in range(len(station_year)):
        t = TaipeiStationInOut.objects.create(name=station_name, year=station_year[i], io_class="進站", io_amount=station_in[i])

    for i in range(len(station_year)):
        t = TaipeiStationInOut.objects.create(name=station_name, year=station_year[i], io_class="出站", io_amount=station_out[i])

    station_data.clear()
    inconnect_year.clear()
print("Done")