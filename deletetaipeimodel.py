import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()
from mainsite.models import TaipeiStationExtraData

data = TaipeiStationExtraData.objects.all()
data.delete()

print('Done')