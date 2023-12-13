from django import forms
from .models import Stock


class StockSelectionForm(forms.Form):
    stock_symbol = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        to_field_name='ticker_symbol',
        label='Select Stock Symbol',
        empty_label='Choose a stock',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
