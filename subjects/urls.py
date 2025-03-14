from django.urls import path
from . import views

urlpatterns = [
    path('', views.subjects_management, name='subjects_management'),
    path('edit_class/<int:id>/', views.edit_class, name='edit_class'),
    path('delete_class/<int:id>/', views.delete_class, name='delete_class'),
    path('edit_section/<int:id>/', views.edit_section, name='edit_section'),
    path('delete_section/<int:id>/', views.delete_section, name='delete_section'),
    path('edit_subject/<int:id>/', views.edit_subject, name='edit_subject'),
    path('delete_subject/<int:id>/', views.delete_subject, name='delete_subject'),
    path('edit_subject_assign/<int:id>/', views.edit_subject_assign, name='edit_subject_assign'),
    path('delete_subject_assign/<int:id>/', views.delete_subject_assign, name='delete_subject_assign'),
]