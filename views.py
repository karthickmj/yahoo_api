from django.views import View
from django.http import JsonResponse
from .yahoo import Ticker


class StockDataView(View):
    def get(self, request, ticker_symbol):
        ticker = Ticker(ticker_symbol)
        summary_data = ticker.summary()
        return JsonResponse(summary_data)
