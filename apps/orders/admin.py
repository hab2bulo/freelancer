# Django admin moduli
from django.contrib import admin

# Order modelini import qilamiz
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Admin list sahifada ko‘rinadigan ustunlar
    list_display = (
        'id',
        'client',
        'freelancer',
        'status',
        'price',
        'created_at',
    )

    # Status bo‘yicha tez filtr qilish
    list_filter = ('status',)

    # Admin search oynasi uchun
    search_fields = ('client__username', 'freelancer__username')

    # Admin list sahifada pagination
    list_per_page = 20

        Service,
        on_delete=models.CASCADE,     # service o‘chsa order ham o‘chadi
