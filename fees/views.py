from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FeesGroup, FeesType
from .forms import FeesGroupForm, FeesTypeForm
from .models import FeesPayment

def fees_carry_forward(request):
    return render(request, 'fees/fees_carry_forward.html')

def fees_setup(request):
    fees_groups = FeesGroup.objects.all()
    fees_types = FeesType.objects.all()
    group_form = FeesGroupForm()
    type_form = FeesTypeForm()

    return render(request, 'fees/fees_setup.html', {  # ✅ Correct path
        'fees_groups': fees_groups,
        'fees_types': fees_types,
        'group_form': group_form,
        'type_form': type_form
    })


def add_fees_group(request):
    if request.method == "POST":
        form = FeesGroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fees Group added successfully!")
        else:
            messages.error(request, "Invalid data!")
    return redirect('fees_setup')

def edit_fees_group(request, group_id):
    group = get_object_or_404(FeesGroup, id=group_id)
    if request.method == "POST":
        form = FeesGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, "Fees Group updated successfully!")
    return redirect('fees_setup')


def add_fees_type(request):
    if request.method == "POST":
        form = FeesTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fees Type added successfully!")
        else:
            messages.error(request, "Invalid data!")
    return redirect('fees_setup')

def edit_fees_type(request, type_id):
    fee_type = get_object_or_404(FeesType, id=type_id)
    if request.method == "POST":
        form = FeesTypeForm(request.POST, instance=fee_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Fees Type updated successfully!")

def fees_setup(request):
    fees_groups = FeesGroup.objects.all()
    fees_types = FeesType.objects.all()
    group_form = FeesGroupForm()
    type_form = FeesTypeForm()

    # ✅ सभी FeesGroup के लिए उनके amount type निकालना
    amount_type_dict = {group.id: group.amount_type for group in fees_groups}

    return render(request, 'fees_setup.html', {
        'fees_groups': fees_groups,
        'fees_types': fees_types,
        'group_form': group_form,
        'type_form': type_form,
        'amount_type_dict': amount_type_dict
    })

def delete_fees_group(request, group_id):
    group = get_object_or_404(FeesGroup, id=group_id)
    group.delete()
    messages.success(request, "Fees Group deleted successfully!")
    return redirect('fees_setup')


def delete_fees_type(request, type_id):
    fee_type = get_object_or_404(FeesType, id=type_id)
    fee_type.delete()
    messages.success(request, "Fees Type deleted successfully!")
    return redirect('fees_setup')
