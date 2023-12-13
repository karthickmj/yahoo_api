from django.urls import path
from .views import StockDataView, FetchStockData

urlpatterns = [
    path('stock-data/', StockDataView.as_view(), name='stock_data'),
    path('fetch-stock-data/<str:ticker_symbol>/', FetchStockData.as_view(), name='fetch_stock_data'),
]