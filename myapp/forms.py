from django import forms
from .models import Doctors , Payments

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['name', 'age', 'specialization', 'experience', 'timings', 'salary', 'charge']

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ['patient_name','medical_bill','hospital_bill','discharge_date']






