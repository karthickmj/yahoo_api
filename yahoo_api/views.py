from django.shortcuts import render
from django.views import View
from .forms import StockTickerForm
from .utils import get_stock_data


class StockDataView(View):
    template_name = 'stock_data.html'

    def get(self, request, *args, **kwargs):
        form = StockTickerForm()
        return render(request, self.template_name, {'StockTickerForm': form})

    def post(self, request, *args, **kwargs):
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            data = get_stock_data(ticker)
            return render(request, self.template_name, {'StockTickerForm': form, 'data': data})
        return render(request, self.template_name, {'StockTickerForm': form})
