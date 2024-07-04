from django.db import models

class Doctors(models.Model):
    name = models.CharField(max_length=20)
    age = models.DecimalField(max_digits=2, decimal_places=0)
    specialization = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=5, decimal_places=0)
    timings = models.CharField(max_length=20)
    charge = models.DecimalField(max_digits=5,decimal_places=0)

class Payments(models.Model):
    patient_name = models.CharField(max_length=20)
    medical_bill = models.DecimalField(max_digits=10,decimal_places=2)
    hospital_bill = models.DecimalField(max_digits=10,decimal_places=2)
    discharge_date = models.DateField()




