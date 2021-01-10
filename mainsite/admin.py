from django.contrib import admin
from mainsite.models import AccessInfo, PlayList, TaipeiStationExtraData, TaipeiStationInOut

class TaipeiStationExtraDataAdmin(admin.ModelAdmin):
   list_display = ('year_date', 'total_mileage', 'total_persontimes', 'total_income')
admin.site.register(TaipeiStationExtraData, TaipeiStationExtraDataAdmin)

class TaipeiStationInOutAdmin(admin.ModelAdmin):
   list_display = ('name', 'year', 'io_class', 'io_amount')
admin.site.register(TaipeiStationInOut, TaipeiStationInOutAdmin)



class PostAdmin(admin.ModelAdmin):
   list_display = ('name','picture','video','wiki','pub_date')
admin.site.register(PlayList, PostAdmin)

class PostAdmin(admin.ModelAdmin):
   list_display = ('title','slug','pub_date')
admin.site.register(AccessInfo)
