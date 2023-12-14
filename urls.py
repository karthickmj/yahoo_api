from django.urls import path
from .views import StockDetailView

urlpatterns = [
    # ... other url patterns ...
    path('stock/<str:ticker_symbol>/', StockDetailView.as_view(), name='stock_detail'),
]