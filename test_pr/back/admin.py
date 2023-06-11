from django.contrib import admin
from back.models import Contract, CreditOrder, Producer, Product


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['created_at']
    list_filter = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name', 'producer', 'credit_order']
    list_filter = ['created_at', 'name', 'producer', 'credit_order']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'name']
    list_filter = ['created_at', 'name']


@admin.register(CreditOrder)
class CreditOrderAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'contract']
    list_filter = ['created_at', 'contract']



