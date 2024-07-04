from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_data, name='doctor_data'),
    path('doctors/<int:doctor_id>/', views.read_doctor, name='read_doctor'),
    path('doctors/update/<int:doctor_id>/', views.update_doctor, name='update_doctor'),
    path('doctors/partial-update/<int:doctor_id>/', views.partial_update_doctor, name='partial_update_doctor'),
    path('payments/post/',views.payments_post,name='payments_post')
]