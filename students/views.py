from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    search_query = request.GET.get('search', '')
    students = Student.objects.all()
    if search_query:
        students = students.filter(
            first_name__icontains=search_query
        ) | students.filter(
            last_name__icontains=search_query
        ) | students.filter(
            mobile_number__icontains=search_query
        ) | students.filter(
            email__icontains=search_query
        )
    return render(request, 'students/students_list.html', {'students': students, 'search_query': search_query})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/add_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})