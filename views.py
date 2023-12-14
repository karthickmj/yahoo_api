from django.http import JsonResponse
from .forms import StockSelectionForm
from .yahoo import ticker


def StockDataView(request):
    if request.method == 'POST':
        form = StockSelectionForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['stock']
            ticker_symbol = stock.ticker_symbol
            data = ticker.get_summary_data(ticker_symbol)
            return JsonResponse(data)
    else:
        form = StockSelectionForm()
    return JsonResponse({'error': 'Invalid method or form data'}, status=400)
