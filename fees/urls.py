from django.urls import path
from .views import fees_carry_forward  # सुनिश्चित करें कि यह इम्पोर्ट किया गया है
from .views import fees_setup, add_fees_group, add_fees_type, edit_fees_group, edit_fees_type, delete_fees_group, delete_fees_type

urlpatterns = [
    path('carry-forward/', fees_carry_forward, name='fees_carry_forward'),
    path('setup/', fees_setup, name='fees_setup'),
    path('add-fees-group/', add_fees_group, name='add_fees_group'),
    path('add-fees-type/', add_fees_type, name='add_fees_type'),
    path('edit-fees-group/<int:group_id>/', edit_fees_group, name='edit_fees_group'),
    path('edit-fees-type/<int:type_id>/', edit_fees_type, name='edit_fees_type'),
    path('delete-fees-group/<int:group_id>/', delete_fees_group, name='delete_fees_group'),
    path('delete-fees-type/<int:type_id>/', delete_fees_type, name='delete_fees_type'),
]
