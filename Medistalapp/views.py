from django.shortcuts import render, redirect
from Medistalapp.models import Company, Patient , Appointment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'About.html')


def services(request):
    return render(request, 'Services.html')


def appointment(request):
    return render(request, 'appointment.html')


def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def contacts(request):
    if request.method == 'POST':
        contacts = Company(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'])
        contacts.save()
        return redirect('/contacts')
    else:
        return render(request, 'Contacts.html')
def patients(request):
    if request.method == 'POST':
        patients = Patient(fullname=request.POST['fullname'],
                           email=request.POST['email'],
                           medhistory=request.POST['medhistory'],)
        patients.save()
        return redirect('/patients')
    else:
        return render(request, 'Patients.html')

def appoint(request):
    if request.method == 'POST':
        appointments = Appointment(name=request.POST['name'],
                                   email=request.POST['email'],
                                   phone=request.POST['phone'],
                                   date=request.POST['date'],
                                   department=request.POST['department'],
                                   doctor=request.POST['doctor'],
                                   message=request.POST['message'],)
        appointments.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

def show(request):
    data = Appointment.objects.all()
    return render(request, 'Show.html', {'appointment':data})

def delete(request,id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')













