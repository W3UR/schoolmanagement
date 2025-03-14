from django.urls import path
from . import views

urlpatterns = [
    path('', views.transport_management, name='transport_management'),
    path('delete-route/<int:route_id>/', views.delete_route, name='delete_route'),
    path('delete-stoppage/<int:stoppage_id>/', views.delete_stoppage, name='delete_stoppage'),
    path('delete-assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
]
