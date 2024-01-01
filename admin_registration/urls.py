# urls.py
from django.urls import path
from .views import admin_registration
from .views import CustomPasswordResetConfirmView

urlpatterns = [
    # existing patterns
    path('admin-registration/', admin_registration, name='admin_registration'),

    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
