from django.urls import path
from . import views

urlpatterns = [
    # path('cars/toyota/', views.toyota_cars, name='toyota_cars'),
    # path('cars/bmw/', views.bmw_cars, name='bmw_cars'),
    # path('cars/volkswagen/', views.volkswagen_cars, name='volkswagen_cars')
    path('brand/<str:brand_slug>/', views.brand_cars, name='brand_cars')
]
