from django.views.generic import View
from django.shortcuts import render
from .forms import StockSelectionForm
from .yahoo import ticker


class StockDataView(View):
    template_name = 'stock_data.html'

    def get(self, request, *args, **kwargs):
        form = StockSelectionForm()
        return render(request, self.template_name, {'StockSelectionForm': form})

    def post(self, request, *args, **kwargs):
        form = StockSelectionForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data['ticker_symbol']
            stock_data = ticker.get_data(ticker_symbol)
            return render(request, self.template_name, {'stock_data': stock_data, 'StockSelectionForm': form})
        else:
            return render(request, self.template_name, {'StockSelectionForm': form})
