from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker_symbol', 'name', 'price', 'last_updated')
    search_fields = ('ticker_symbol', 'name')

# Alternatively, you can use admin.site.register()
# admin.site.register(Stock, StockAdmin)
