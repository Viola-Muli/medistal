
from django.contrib import admin
from django.urls import path
from Medistalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('start/',views.starter,name='start'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('departments/',views.departments,name='departments'),
    path('doctors/',views.doctors,name='doctors'),
    path('contacts/',views.contacts,name='contacts'),
    path('patients/',views.patients,name='patients'),
    path('appointment/', views.appoint, name='appointments'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
