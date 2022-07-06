from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Patient_info, Address
from .forms import Patient_info_form, Patient_nok_form, Patient_address_form
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def record_home(request):
    patient_form = Patient_info_form()
    context ={'patient_form':patient_form}
    return render(request, 'recordapp/home1.html', context)

@login_required   
def view_all_patients(request):
    all_patient= Patient_info.objects.all()
    context = {'all_patient' : all_patient}
    return render(request, 'recordapp/view-all-patients1.html', context )
@login_required
def add_patient(request): 
    if request.method =="POST":
        patient_form = Patient_info_form(request.POST)
        if patient_form.is_valid():
            patientid=patient_form.save()
            patient_details = patientid.id
            messages.success(request, "Patient Details added  successfully." )
            return redirect('recordapp:add-address', pk=patient_details)
        else:
            messages.error(request, "Patient hospital No or email address already exist")
            context ={'patient_form':patient_form}
            return render(request, 'recordapp/add-new-patients1.html', context)

    else: 
        patient_form = Patient_info_form()    
        context ={'patient_form':patient_form}
        return render(request, 'recordapp/add-new-patients1.html', context)
@login_required
def update_details(request, id):
    get_user_data = get_object_or_404(Patient_info, pk=id)
    patient_form = Patient_info_form(instance=get_user_data)
    if request.method == 'POST':
        form = Patient_info_form(request.POST, instance=get_user_data)
        if form.is_valid():
            patientid=form.save()
            patient_details = patientid.id
            messages.success(request, 'patient details updated')
        return redirect('recordapp:patient-details', pk=patient_details)

    context = { 'patient_form':patient_form }
    return render(request, 'recordapp/update-details.html', context)

@login_required      
def patient_details(request, pk):
    patient_details = Patient_info.objects.get(id=pk)
    try:
        patient_address = Address.objects.get(patient_info=pk)
        context = {'patient_details' : patient_details, 'patient_address':patient_address, 'address_id':address_id}
        template_name = 'recordapp/patientProfile.html'
        return render(request, template_name, context)
    except Address.DoesNotExist:
        context = {'patient_details' : patient_details}
        template_name = 'recordapp/patientProfile.html'
        return render(request, template_name, context)

    
@login_required
def delete_details(request, id):
    get_user = get_object_or_404(Patient_info, pk=id)
    if request.method == 'POST':
        get_user.delete()
        messages.error(request, 'User deleted')
        return redirect('recordapp:all-patients')
    return render(request, 'recordapp/delete-patient.html', {})
    
def success(request):
    return render(request, 'recordapp/success.html', { })
# new patient end
# Nok for patient start
@login_required
def addnok(request, pk):
    patient_det = Patient_info.objects.get(id=pk)
    patient_nok_form = Patient_nok_form()
    if request.method =="POST":
        patient_nok_form = Patient_nok_form(request.POST)
        if patient_nok_form.is_valid():
            patientid=patient_nok_form.save(commit=False)
            patientid.personal_info = patient_det
            patientid.save()
            patient_det = patient_det.pk
            messages.success(request, "NOK Registration was successful." )
        return redirect('recordapp:patient-details', pk=patient_det)
        

    context = {'patient_details' : patient_det, 'nok_form':patient_nok_form}
    return render(request, 'recordapp/nok.html', context)
# nok for  patient end
# Address for patient start
@login_required
def add_address(request, pk):
    patient_det = Patient_info.objects.get(id=pk)
    patient_address= Patient_address_form(instance=patient_det)
    if request.method =="POST":
        patient_address_form = Patient_address_form(request.POST)
        if patient_address_form.is_valid():
            patientid=patient_address_form.save(commit=False)
            patientid.patient_info = patient_det
            patientid.save()
            patient_det = patient_det.pk
            messages.success(request, "Address Registration was successful." )
        return redirect('recordapp:patient-details', pk=patient_det)
        

    context = {'patient_address' : patient_address, 'patient_det':patient_det}
    return render(request, 'recordapp/address.html', context)
# Address for  patient end

@login_required
def rank(request, pk):
    patient_det = Patient_info.objects.get(id=pk)
    patient_address_form = Patient_address_form()
    if request.method =="POST":
        patient_address_form = Patient_address_form(request.POST)
        if patient_address_form.is_valid():
            patientid=patient_address_form.save(commit=False)
            patientid.personal_info = patient_det
            patientid.save()
            patient_det = patient_det.pk
            messages.success(request, "Address Registration was successful." )
        return redirect('recordapp:patient-details', pk=patient_det)
        

    context = {'patient_details' : patient_det, 'address_form':patient_address_form}
    return render(request, 'recordapp/address.html', context)
# Address for  patient end
# unit for  patient start

@login_required
def add_unit(request, pk):
    context={}
    return render(request, 'recordapp/unit.html', context)
# unit for  patient end
# rank for  patient start
@login_required
def add_rank(request, pk):
    context={}
    return render(request, 'recordapp/rank.html', context)
# rank for  patient end
@login_required
def open_folder(request):
    return render(request, 'recordapp/openfolder.html', {})     