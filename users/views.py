from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser
from .forms import UserRegistrationForm, UserProfileForm, UserRoleUpdateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm  # ✅ इम्पोर्ट किया गया

# सुपर एडमिन चेक करने का फंक्शन
def is_super_admin(user):
    return user.is_superuser

# ✅ यूजर रजिस्ट्रेशन फंक्शन
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "रजिस्ट्रेशन सफल हुआ!")
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# ✅ लॉगिन फंक्शन (अब सही किया गया)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "लॉगिन सफल हुआ!")
            return redirect('dashboard')
        else:
            messages.error(request, "अमान्य लॉगिन विवरण!")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# ✅ लॉगआउट फंक्शन
def user_logout(request):
    logout(request)
    messages.success(request, "आप लॉगआउट हो गए!")
    return redirect('login')

# ✅ यूजर प्रोफाइल फंक्शन
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "प्रोफाइल अपडेट हो गई!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

# ✅ सुपर एडमिन के लिए यूजर मैनेजमेंट पेज
@login_required
@user_passes_test(is_super_admin)
def user_management_view(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_management.html', {'users': users})

# ✅ यूजर डिलीट करने का फंक्शन
@login_required
@user_passes_test(is_super_admin)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, "यूजर को सफलतापूर्वक डिलीट कर दिया गया!")
    return redirect('user_management')

# ✅ यूजर का रोल अपडेट करने का फंक्शन
@login_required
@user_passes_test(is_super_admin)
def update_user_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserRoleUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "यूजर का रोल अपडेट हो गया!")
            return redirect('user_management')
    else:
        form = UserRoleUpdateForm(instance=user)
    return render(request, 'users/update_user_role.html', {'form': form, 'user': user})
