from django.contrib import admin

from customers.models import Customer

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    pass
