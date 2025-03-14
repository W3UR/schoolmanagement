from django.urls import path
from .views import (
    register, user_login, user_logout, profile_view,
    user_management_view, delete_user, update_user_role
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('manage-users/', user_management_view, name='user_management'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('update-user-role/<int:user_id>/', update_user_role, name='update_user_role'),
]
