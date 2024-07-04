from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Doctors
from .forms import DoctorForm
import json

@csrf_exempt
def doctor_data(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse({
                'id': item.id,
                'name': item.name,
                'age': item.age,
                'specialization': item.specialization,
                'experience': item.experience,
                'salary': item.salary,
                'timings': item.timings,
                'charge': item.charge
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return HttpResponseBadRequest("Invalid HTTP method.")

@csrf_exempt
def read_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctors, pk=doctor_id)
    return JsonResponse({
        'id': doctor.id,
        'name': doctor.name,
        'age': doctor.age,
        'specialization': doctor.specialization,
        'experience': doctor.experience,
        'salary': doctor.salary,
        'timings': doctor.timings,
        'charge': doctor.charge
    })

@csrf_exempt
def update_doctor(request, doctor_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON.")

        doctor = get_object_or_404(Doctors, pk=doctor_id)
        form = DoctorForm(data, instance=doctor)
        if form.is_valid():
            item = form.save()
            return JsonResponse({
                'id': item.id,
                'name': item.name,
                'age': item.age,
                'specialization': item.specialization,
                'experience': item.experience,
                'salary': item.salary,
                'timings': item.timings,
                'charge': item.charge
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return HttpResponseBadRequest("Invalid HTTP method.")

@csrf_exempt
def partial_update_doctor(request, doctor_id):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON.")

        doctor = get_object_or_404(Doctors, pk=doctor_id)
        form = DoctorForm(data, instance=doctor, partial=True)  # partial=True for partial updates
        if form.is_valid():
            item = form.save()
            return JsonResponse({
                'id': item.id,
                'name': item.name,
                'age': item.age,
                'specialization': item.specialization,
                'experience': item.experience,
                'salary': item.salary,
                'timings': item.timings,
                'charge': item.charge
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return HttpResponseBadRequest("Invalid HTTP method.")





















# from django.shortcuts import render , get_object_or_404
# from django.http import HttpResponse , JsonResponse
# from .forms import DoctorForm
# from django.views.decorators.csrf import csrf_exempt
# from .models import Doctors
# import json



# # Create your views here.
# def hello(request):
#     return HttpResponse('hello , this the first sample page fpr the hospital')

# from django.shortcuts import get_object_or_404
# from django.http import JsonResponse, HttpResponseBadRequest
# from django.views.decorators.csrf import csrf_exempt
# from .models import Doctors
# from .forms import DoctorForm

# @csrf_exempt
# def doctor_data(request):
#     if request.method == 'POST':
#         form = DoctorForm(request.POST)
#         if form.is_valid():
#             item = form.save()
#             return JsonResponse({
#                 'id': item.id,
#                 'name': item.name,
#                 'age': item.age,
#                 'specialization': item.specialization,
#                 'experience': item.experience,
#                 'salary': item.salary,
#                 'timings': item.timings,
#                 'charge': item.charge
#             })
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)
#     else:
#         return HttpResponseBadRequest("Invalid HTTP method.")

# @csrf_exempt
# def read_doctor(request, doctor_id):
#     doctor = get_object_or_404(Doctors, pk=doctor_id)
#     return JsonResponse({
#         'id': doctor.id,
#         'name': doctor.name,
#         'age': doctor.age,
#         'specialization': doctor.specialization,
#         'experience': doctor.experience,
#         'salary': doctor.salary,
#         'timings': doctor.timings,
#         'charge': doctor.charge
#     })


# @csrf_exempt
# def update_doctor(request, doctor_id):
#     if request.method == 'POST':
#         doctor = get_object_or_404(Doctors, pk=doctor_id)
#         form = DoctorForm(request.POST, instance=doctor)
#         if form.is_valid():
#             item = form.save()
#             return JsonResponse({
#                 'id': item.id,
#                 'name': item.name,
#                 'age': item.age,
#                 'specialization': item.specialization,
#                 'experience': item.experience,
#                 'salary': item.salary,
#                 'timings': item.timings,
#                 'charge': item.charge
#             })
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)
#     else:
#         return HttpResponseBadRequest("Invalid HTTP method.")
    
# @csrf_exempt
# def partial_update_doctor(request, doctor_id):
#     if request.method == 'PATCH':
#         try:
#             data = json.loads(request.body)
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest("Invalid JSON.")

#         doctor = get_object_or_404(Doctors, pk=doctor_id)
#         form = DoctorForm(data, instance=doctor, partial=True)  # partial=True for partial updates
#         if form.is_valid():
#             item = form.save()
#             return JsonResponse({
#                 'id': item.id,
#                 'name': item.name,
#                 'age': item.age,
#                 'specialization': item.specialization,
#                 'experience': item.experience,
#                 'salary': item.salary,
#                 'timings': item.timings,
#                 'charge': item.charge
#             })
#         else:
#             return JsonResponse({'errors': form.errors}, status=400)
#     else:
#         return HttpResponseBadRequest("Invalid HTTP method.")



