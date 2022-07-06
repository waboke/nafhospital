from django.db import models
from recordapp.models import Patient_info

# Create your models here.
class open_folder(models.Model):
    patient_info =models.ForeignKey(Patient_info, on_delete=models.CASCADE)
    open_folder = models.BooleanField(default=False)
    Opened_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    # closed_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    
    
    
    