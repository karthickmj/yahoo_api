from django import forms
from .models import StockTicker


class StockTickerForm(forms.Form):
    ticker = forms.ModelChoiceField(queryset=StockTicker.objects.all(),
                                     empty_label="Select a Stock Ticker")
