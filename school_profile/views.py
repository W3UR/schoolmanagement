from django.shortcuts import render, redirect, get_object_or_404
from .models import SchoolProfile
from .forms import SchoolProfileForm

def school_profile_view(request):
    profile = SchoolProfile.objects.first()  # पहला रिकॉर्ड लोड करें
    return render(request, 'school_profile/profile_view.html', {'profile': profile})

def school_profile_edit(request):
    profile = SchoolProfile.objects.first()  # पहला रिकॉर्ड लोड करें या नया बनाएं
    if request.method == 'POST':
        form = SchoolProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('school_profile_view')  # सेव करने के बाद व्यू पेज पर जाएं
    else:
        form = SchoolProfileForm(instance=profile)
    return render(request, 'school_profile/profile_form.html', {'form': form})
