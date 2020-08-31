from django.contrib import admin
from .models import Product, Order, CheckOutOrder


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'amount', 'price')
    list_display_links = ('pk', 'name')
    list_filter = ('category',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(CheckOutOrder)
