from django.urls import path
from . import views
from .views import quickview_detail


urlpatterns = [
				path('', views.accessories_list, name='our_products'),
				path('accessories/', views.accessory, name='accessories'),
				path('<int:accessory_id>/', views.accessory_detail, name='accessory_details'),
				path('filter-accessories/', views.filter_accessories, name='filter_accessories'),
				path('quickview/<int:accessory_id>/', quickview_detail, name='quick_view'),
				path('send-email/', views.send_email, name='send_email'),
				path('search/', views.search_accessory, name='search_accessory'),

]

