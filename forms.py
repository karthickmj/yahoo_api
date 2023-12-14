from django import forms

# Assuming 'get_stock_symbols' is a function that fetches stock symbols
# from an external source or a predefined list.
from .utils import get_stock_symbols

class StockSelectForm(forms.Form):
    stock_symbol = forms.ChoiceField(choices=[], label='Select Stock Symbol')

    def __init__(self, *args, **kwargs):
        super(StockSelectForm, self).__init__(*args, **kwargs)
        self.fields['stock_symbol'].choices = get_stock_symbols()
