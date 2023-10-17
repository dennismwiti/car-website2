from django.contrib import admin
from .models import Accessories


# Register your models here.
class AccessoryAdmin(admin.ModelAdmin):
				list_display = ('name', 'category', 'type_slug', 'price', 'features', 'is_featured', 'is_special',)
				list_filter = ('name', 'type_slug', 'category',)
				search_fields = ('name',)


admin.site.register(Accessories, AccessoryAdmin)
