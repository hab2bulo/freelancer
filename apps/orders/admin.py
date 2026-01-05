from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'freelancer',
        'status',
        'created_at',
    )

    list_filter = ('status',)
    search_fields = ('client__username', 'freelancer__username')
