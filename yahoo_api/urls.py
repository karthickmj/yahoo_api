from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stock_data/<str:ticker_symbol>/', views.StockDataView, name='StockDataView'),
]