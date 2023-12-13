from django import forms
from .models import StockTicker


class StockTickerForm(forms.Form):
    ticker = forms.ModelChoiceField(
        queryset=StockTicker.objects.all(),
        to_field_name='symbol',
        empty_label='Select a stock ticker',
        label='Stock Ticker'
    )
