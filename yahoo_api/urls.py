from django.urls import path
from .views import StockDataView

urlpatterns = [
    # ... your other url patterns here ...
    path('stock-data/', StockDataView.as_view(), name='stock-data'),
]