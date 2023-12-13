from django.urls import path
from .views import StockDataView

urlpatterns = [
    # ... your other url patterns here ...
    path('stocks/', StockDataView.as_view(), name='stock_data'),
]