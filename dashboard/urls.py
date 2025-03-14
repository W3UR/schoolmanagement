from django.contrib import admin
from django.urls import path, include
from .views import dashboard_view, get_fees_data, get_attendance_data, get_students_data

urlpatterns = [
    path('students/', include('students.urls')),
    path('', dashboard_view, name='dashboard'),
    path('api/fees/', get_fees_data, name='api_fees'),
    path('api/attendance/', get_attendance_data, name='api_attendance'),

]
