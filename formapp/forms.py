from django import forms
from .models import Emp
# fields with validation
class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

