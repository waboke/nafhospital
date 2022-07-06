from django.contrib import admin
from .models import open_folder
class FolderAdmin(admin.ModelAdmin):
    list_display = ('patient_info', 'open_folder', 'Opened_date')
    
# Register your models here.
admin.site.register(open_folder, FolderAdmin)
