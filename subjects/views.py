from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, Section, Subject, SubjectAssignment
from .forms import ClassForm, SectionForm, SubjectForm, SubjectAssignmentForm

def subjects_management(request):
    # क्लास
    class_form = ClassForm(request.POST or None)
    if request.method == 'POST' and 'class_submit' in request.POST:
        if class_form.is_valid():
            class_form.save()
            return redirect('subjects_management')

    # सेक्शन
    section_form = SectionForm(request.POST or None)
    if request.method == 'POST' and 'section_submit' in request.POST:
        if section_form.is_valid():
            section_form.save()
            return redirect('subjects_management')

    # सब्जेक्ट
    subject_form = SubjectForm(request.POST or None)
    if request.method == 'POST' and 'subject_submit' in request.POST:
        if subject_form.is_valid():
            subject_form.save()
            return redirect('subjects_management')

    # सब्जेक्ट असाइन
    subject_assign_form = SubjectAssignmentForm(request.POST or None)
    if request.method == 'POST' and 'subject_assign_submit' in request.POST:
        if subject_assign_form.is_valid():
            subject_assign_form.save()
            return redirect('subjects_management')

    context = {
        'class_form': class_form,
        'section_form': section_form,
        'subject_form': subject_form,
        'subject_assign_form': subject_assign_form,
        'classes': Class.objects.all(),
        'sections': Section.objects.all(),
        'subjects': Subject.objects.all(),
        'subject_assignments': SubjectAssignment.objects.all(),
    }
    return render(request, 'subjects/subjects_management.html', context)

# क्लास एडिट और डिलीट
def edit_class(request, id):
    class_obj = get_object_or_404(Class, id=id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect('subjects_management')
    else:
        form = ClassForm(instance=class_obj)
    return render(request, 'subjects/edit_class.html', {'form': form})

def delete_class(request, id):
    class_obj = get_object_or_404(Class, id=id)
    if request.method == 'POST':
        class_obj.delete()
        return redirect('subjects_management')
    return render(request, 'subjects/confirm_delete.html', {'object': class_obj})

# सेक्शन एडिट और डिलीट
def edit_section(request, id):
    section_obj = get_object_or_404(Section, id=id)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section_obj)
        if form.is_valid():
            form.save()
            return redirect('subjects_management')
    else:
        form = SectionForm(instance=section_obj)
    return render(request, 'subjects/edit_section.html', {'form': form})

def delete_section(request, id):
    section_obj = get_object_or_404(Section, id=id)
    if request.method == 'POST':
        section_obj.delete()
        return redirect('subjects_management')
    return render(request, 'subjects/confirm_delete.html', {'object': section_obj})

# सब्जेक्ट एडिट और डिलीट
def edit_subject(request, id):
    subject_obj = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject_obj)
        if form.is_valid():
            form.save()
            return redirect('subjects_management')
    else:
        form = SubjectForm(instance=subject_obj)
    return render(request, 'subjects/edit_subject.html', {'form': form})

def delete_subject(request, id):
    subject_obj = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        subject_obj.delete()
        return redirect('subjects_management')
    return render(request, 'subjects/confirm_delete.html', {'object': subject_obj})

# सब्जेक्ट असाइन एडिट और डिलीट
def edit_subject_assign(request, id):
    subject_assign_obj = get_object_or_404(SubjectAssignment, id=id)
    if request.method == 'POST':
        form = SubjectAssignmentForm(request.POST, instance=subject_assign_obj)
        if form.is_valid():
            form.save()
            return redirect('subjects_management')
    else:
        form = SubjectAssignmentForm(instance=subject_assign_obj)
    return render(request, 'subjects/edit_subject_assign.html', {'form': form})

def delete_subject_assign(request, id):
    subject_assign_obj = get_object_or_404(SubjectAssignment, id=id)
    if request.method == 'POST':
        subject_assign_obj.delete()
        return redirect('subjects_management')
    return render(request, 'subjects/confirm_delete.html', {'object': subject_assign_obj})