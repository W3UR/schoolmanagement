from django.shortcuts import render
from django.http import JsonResponse
from fees.models import FeesPayment
from attendance.models import Attendance
from students.models import Student
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

@login_required
def dashboard_view(request):
    user = request.user
    if user.is_superuser:
        allowed_modules = ['डैशबोर्ड', 'टीचर मैनेजमेंट', 'स्टूडेंट मैनेजमेंट', 'फीस मैनेजमेंट', 'रिपोर्ट्स']
    else:
        allowed_modules = [module.name for module in user.allowed_modules.all()]

    return render(request, 'dashboard.html', {'allowed_modules': allowed_modules})

# 🏠 Dashboard View
def dashboard_view(request):
    return render(request, 'dashboard.html')

# 📊 Fees Collection API
def get_fees_data(request):
    fees_data = FeesCollection.objects.all().order_by('month')
    data = {
        "labels": [fee.month for fee in fees_data],
        "values": [fee.amount for fee in fees_data],
    }
    return JsonResponse(data)

# 📅 Attendance API
def get_attendance_data(request):
    attendance_data = Attendance.objects.latest('date')
    data = {
        "labels": ["हाज़िर", "अनुपस्थित"],
        "values": [attendance_data.present, attendance_data.absent],
    }
    return JsonResponse(data)

# 🎓 Student Enrollment API
def get_students_data(request):
    students_data = StudentEnrollment.objects.all().order_by('year')
    data = {
        "labels": [str(student.year) for student in students_data],
        "values": [student.total_students for student in students_data],
    }
    return JsonResponse(data)
