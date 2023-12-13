from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from .forms import StockSelectionForm
from .yahoo import ticker


class StockDataView(View):
    def get(self, request, *args, **kwargs):
        form = StockSelectionForm()
        return render(request, 'stock_data.html', {'form': form})


class FetchStockData(View):
    def get(self, request, ticker_symbol, *args, **kwargs):
        stock_data = ticker.get_data(ticker_symbol)
        return JsonResponse(stock_data)
