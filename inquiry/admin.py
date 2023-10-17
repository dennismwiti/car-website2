from django.contrib import admin
from .models import Inquiry


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('car_title', 'first_name', 'last_name', 'email', 'customer_need', 'city', 'state',
                    'phone', 'message', 'create_date',)
    list_filter = ('email', 'phone', 'create_date',)
    search_fields = ('id', 'email', 'phone',)


admin.site.register(Inquiry, InquiryAdmin)

# Register your models here.
