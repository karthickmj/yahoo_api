from django import forms


class StockTickerForm(forms.Form):
    ticker_symbol = forms.CharField(label='Stock Ticker', max_length=10)
