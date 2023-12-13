from django.shortcuts import render
from django.views import View
from .forms import StockTickerForm
from .yahoo import ticker


class StockDataView(View):
    template_name = 'stock_data.html'

    def get(self, request, *args, **kwargs):
        form = StockTickerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = StockTickerForm(request.POST)
        if form.is_valid():
            ticker_symbol = form.cleaned_data.get('ticker')
            stock_info = ticker(ticker_symbol)
            return render(request, self.template_name, {
                'form': form,
                'stock_data': stock_info
            })
        return render(request, self.template_name, {'form': form})
