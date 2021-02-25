from django.contrib import admin

from devices.models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
