from django import forms
from Medistalapp.models import Appointment

class Appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields =['name','email','phone','date','department','doctor','message']