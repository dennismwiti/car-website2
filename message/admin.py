from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sender_email', 'product_name', 'customer_need', 'city', 'state',
                    'phone', 'message', 'timestamp',)
    list_filter = ('sender_email', 'phone', 'timestamp',)
    search_fields = ('id', 'sender_email', 'phone',)


admin.site.register(Message, MessageAdmin)
