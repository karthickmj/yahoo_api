from django.views.generic import View
from django.shortcuts import render
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
            stock_symbol = form.cleaned_data.get('symbol')
            stock_data = get_stock_data(stock_symbol)
            if stock_data:
                return render(request, self.template_name, {'stock_data': stock_data, 'form': form})
            else:
                error = 'Could not retrieve data for the provided stock symbol.'
                return render(request, self.template_name, {'error': error, 'form': form})
        else:
            return render(request, self.template_name, {'form': form})
