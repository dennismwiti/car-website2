"""
URL configuration for carseller project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from admin_registration.views import admin_registration
from django.contrib.auth import views as auth_views
from admin_registration.views import CustomPasswordResetConfirmView
# from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-registration/', admin_registration, name='admin_registration'),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('inquiry/', include('inquiry.urls')),
    path('brands/', include('brands.urls')),
    path('our_products/', include('our_products.urls')),
    path('message/', include('message.urls')),

    # add password reset patterns urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # urlpatterns += [
    #     path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    # ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
