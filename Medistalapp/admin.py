from django.contrib import admin
from Medistalapp.models import Product, Patient, Company, Appointment, Member
# Register your models here.
admin.site.register(Product)
admin.site.register(Patient)
admin.site.register(Company)
admin.site.register(Appointment)
admin.site.register(Member)
