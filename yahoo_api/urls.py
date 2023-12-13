from django.urls import path
from .views import StockDataView

urlpatterns = [
    path('stock-data/', StockDataView.as_view(), name='stock-data'),
]