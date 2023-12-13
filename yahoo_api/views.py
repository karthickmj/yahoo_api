from django.shortcuts import render
from django.http import JsonResponse
from .forms import StockTickerForm
from .yahoo import ticker


def index(request):
    if request.method == 'POST':
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data['ticker_symbol']
            return StockDataView(request, ticker_symbol)
    else:
        form = StockTickerForm()
    return render(request, 'index.html', {'StockTickerForm': form})


def StockDataView(request, ticker_symbol):
    if request.method == 'GET':
        stock_ticker = ticker(ticker_symbol)
        summary_data = stock_ticker.summary()
        return JsonResponse(summary_data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
