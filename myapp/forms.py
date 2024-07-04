from django import forms
from .models import Doctors

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['name', 'age', 'specialization', 'experience', 'timings', 'salary', 'charge']





