from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker_symbol', 'name', 'price', 'change', 'percent_change', 'volume')
    search_fields = ('ticker_symbol', 'name')
