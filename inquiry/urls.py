from django.urls import path
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete_inquiry/<int:inquiry_id>/', views.delete_inquiry, name="delete_inquiry"),
]
