from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import StockSelectForm
from .models import Stock
from yahoo import ticker


class StockDetailView(View):
    def get(self, request, ticker_symbol):
        form = StockSelectForm()
        try:
            stock_data = ticker(ticker_symbol).summary()
            stock_stats = ticker(ticker_symbol).statistics()
            stock = Stock(
                name=stock_data['shortName'],
                current_price=stock_data['regularMarketPrice'],
                market_change=stock_data['regularMarketChange'],
                market_change_percent=stock_data['regularMarketChangePercent'],
                financials={
                    'open': stock_stats['open'],
                    'high': stock_stats['dayHigh'],
                    'low': stock_stats['dayLow'],
                    'volume': stock_stats['volume'],
                }
            )
            context = {'form': form, 'stock': stock}
        except Exception as e:
            context = {'form': form, 'error': str(e)}

        return render(request, 'stock_detail.html', context)
