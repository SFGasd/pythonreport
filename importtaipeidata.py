import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

from mainsite.models import TaipeiStationExtraData
with open('taipeiMRTdata.csv', newline='', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    datas = list(rows)[:109]

station_data = list()
inconnect_year = list()
for station in range(1,4):
    for row in datas:
        inconnect_year.append(row[0])
        station_data.append(row[station])

station_year = list(inconnect_year)[1:109]
station_mileage = list(station_data)[1:109]
station_persontimes = list(station_data)[110:218]
station_income = list(station_data)[219:327]

for i in range(len(station_year)):
    t = TaipeiStationExtraData.objects.create(year_date=station_year[i], total_mileage=station_mileage[i], 
    total_persontimes=station_persontimes[i], total_income=station_income[i])

station_data.clear()
inconnect_year.clear()
print("Done")