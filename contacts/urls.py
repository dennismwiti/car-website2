from django.urls import path
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),
    # path('inquiry/dashboard/', views.dashboard, name='dashboard'),

]
