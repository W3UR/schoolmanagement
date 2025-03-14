from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Route, Stoppage, TransportAssignment
from students.models import Student
from .forms import RouteForm, StoppageForm, TransportAssignmentForm

def transport_management(request):
    # Handle Route Form (Add + Edit)
    if 'edit_route_id' in request.GET:
        route = get_object_or_404(Route, id=request.GET.get('edit_route_id'))
        route_form = RouteForm(request.POST or None, instance=route)
    else:
        route_form = RouteForm(request.POST or None)

    if request.method == 'POST' and 'route_submit' in request.POST:
        if route_form.is_valid():
            route_form.save()
            messages.success(request, "✅ Route saved successfully!")
            return redirect('transport_management')

    # Handle Stoppage Form (Add + Edit)
    if 'edit_stoppage_id' in request.GET:
        stoppage = get_object_or_404(Stoppage, id=request.GET.get('edit_stoppage_id'))
        stoppage_form = StoppageForm(request.POST or None, instance=stoppage)
    else:
        stoppage_form = StoppageForm(request.POST or None)

    if request.method == 'POST' and 'stoppage_submit' in request.POST:
        if stoppage_form.is_valid():
            stoppage_form.save()
            messages.success(request, "✅ Stoppage saved successfully!")
            return redirect('transport_management')

    # Handle Transport Assignment Form (Add + Edit)
    if 'edit_assignment_id' in request.GET:
        assignment = get_object_or_404(TransportAssignment, id=request.GET.get('edit_assignment_id'))
        assignment_form = TransportAssignmentForm(request.POST or None, instance=assignment)
    else:
        assignment_form = TransportAssignmentForm(request.POST or None)

    if request.method == 'POST' and 'assignment_submit' in request.POST:
        if assignment_form.is_valid():
            assignment_form.save()
            messages.success(request, "✅ Transport Assignment saved successfully!")
            return redirect('transport_management')

    context = {
        'route_form': route_form,
        'stoppage_form': stoppage_form,
        'assignment_form': assignment_form,
        'routes': Route.objects.all(),
        'stoppages': Stoppage.objects.all(),
        'assignments': TransportAssignment.objects.all(),
    }
    return render(request, 'transport/transport_management.html', context)

# ✅ Edit & Delete Functions
def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    messages.success(request, "✅ Route deleted successfully!")
    return redirect('transport_management')

def delete_stoppage(request, stoppage_id):
    stoppage = get_object_or_404(Stoppage, id=stoppage_id)
    stoppage.delete()
    messages.success(request, "✅ Stoppage deleted successfully!")
    return redirect('transport_management')

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(TransportAssignment, id=assignment_id)
    assignment.delete()
    messages.success(request, "✅ Transport assignment deleted successfully!")
    return redirect('transport_management')
