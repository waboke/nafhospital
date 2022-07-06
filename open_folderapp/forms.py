from django import forms
from . models import open_folder


class open_close_folder_form(forms.ModelForm):
    open_folder = forms.BooleanField(
    widget=forms.CheckboxInput(
        attrs={
            'checked': False,
            'name':'my-checkbox'
        }
    )
  )
    class Meta:
        model = open_folder
        fields =['open_folder']