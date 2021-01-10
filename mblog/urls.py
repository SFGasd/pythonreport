from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, taipei, taipeistationchart, taipeistationincomechart, taipeistationmileagechart, taipeistationpersontimeschart , taipeicar
from mainsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playlist/', views.playlist),
    path('taipeicar/', views.playlist),
    path('taipei/', taipei),
    path('taipeicar/', taipeicar),
    path('taipeistationinout/<int:sta_num>/', taipeistationchart),
    path('taipeistationmileage/<int:mileage_id>/', taipeistationmileagechart),
    path('taipeistationpersontimes/<int:persontimes_id>/', taipeistationpersontimeschart),
    path('taipeistationincome/<int:income_id>/', taipeistationincomechart),
    path('', homepage),
]
