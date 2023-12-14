from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import StockSelectForm
from .models import Stock
from .yahoo import ticker


class StockDetailView(View):
    def get(self, request, ticker_symbol):
        try:
            stock_data = ticker(ticker_symbol)
            summary_data = stock_data.summary()
            statistics_data = stock_data.statistics()

            stock = Stock(
                name=summary_data.get('shortName'),
                current_price=summary_data.get('regularMarketPrice'),
                market_change=summary_data.get('regularMarketChange'),
                market_change_percent=summary_data.get('regularMarketChangePercent'),
                financials={
                    'open': statistics_data.get('open'),
                    'high': statistics_data.get('dayHigh'),
                    'low': statistics_data.get('dayLow'),
                    'volume': statistics_data.get('volume'),
                }
            )

            context = {
                'stock': stock,
                'StockSelectForm': StockSelectForm()
            }
            return render(request, 'templates/stock_detail.html', context)
        except Exception as e:
            return HttpResponse(f'<div class="alert alert-danger">An error occurred: {e}</div>')
