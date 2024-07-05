
from django.contrib import admin
from django.urls import path
from Medistalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('start/',views.starter,name='start'),
]
