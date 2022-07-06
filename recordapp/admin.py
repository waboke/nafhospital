from django.contrib import admin

# Register your models here.
from .models import Patient_info, patient_pic, DependantsCivilianNHIS, Next_of_kin, Address, DependantsPersonnels, CivillianNHISDetails,Personnel_record


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('hospitalNo', 'fname', 'mname','lname', 'data_of_birth', 'sex', 'email')
    
admin.site.register(Patient_info, PatientAdmin)
class PatientPic(admin.ModelAdmin):
    pass
admin.site.register(patient_pic, PatientPic)

admin.site.register(Personnel_record)
admin.site.register(Address)
admin.site.register(Next_of_kin)
admin.site.register(DependantsCivilianNHIS)
admin.site.register(CivillianNHISDetails)
admin.site.register(DependantsPersonnels)