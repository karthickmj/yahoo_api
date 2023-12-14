from django.shortcuts import render
from django.views import View
from .forms import StockSelectForm
from .ticker import get_stock_data


class StockDataView(View):
    template_name = 'stock_data.html'

    def get(self, request, *args, **kwargs):
        form = StockSelectForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = StockSelectForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data['ticker']
            stock_data = get_stock_data(ticker_symbol)
            return render(request, self.template_name, {'form': form, 'stock_data': stock_data})
        return render(request, self.template_name, {'form': form})
