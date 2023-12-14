from django.urls import path
from .views import StockDataView

urlpatterns = [
    # ... your other url patterns ...
    path('stocks/data/<str:ticker_symbol>/', StockDataView.as_view(), name='stock_data'),
]