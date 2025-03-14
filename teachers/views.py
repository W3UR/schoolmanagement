from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from .forms import TeacherForm  # फ़ॉर्म इंपोर्ट करना न भूलें
from django.contrib import messages

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        qualification = request.POST['qualification']
        joining_date = request.POST['joining_date']
        photo = request.FILES.get('photo')
        resume = request.FILES.get('resume')
        joining_letter = request.FILES.get('joining_letter')

        # Duplicate email check
        if Teacher.objects.filter(email=email).exists():
            messages.error(request, "ईमेल पहले से मौजूद है!")
            return redirect('add_teacher')

        Teacher.objects.create(
            name=name, mobile=mobile, email=email,
            qualification=qualification, joining_date=joining_date,
            photo=photo, resume=resume, joining_letter=joining_letter
        )
        messages.success(request, f"{name} को सफलतापूर्वक जोड़ा गया!")
        return redirect('teacher_list')

    return render(request, 'teachers/add_teacher.html')


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)  # ID से टीचर खोजें

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # लिस्ट पेज पर रीडायरेक्ट करें
    else:
        form = TeacherForm(instance=teacher)  # पहले से भरी हुई जानकारी दिखाएं

    return render(request, 'teachers/edit_teacher.html', {'form': form})

def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    messages.success(request, "टीचर को सफलतापूर्वक हटाया गया!")
    return redirect('teacher_list')
