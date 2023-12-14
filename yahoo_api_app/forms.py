from django import forms

# Assuming we have a function to fetch stock symbols
# from an external source or a predefined list
from .utils import get_stock_symbols


class StockSelectForm(forms.Form):
    stock_symbol = forms.ChoiceField(choices=[], label='Select Stock Symbol')

    def __init__(self, *args, **kwargs):
        super(StockSelectForm, self).__init__(*args, **kwargs)
        self.fields['stock_symbol'].choices = get_stock_symbols()

# Example utility function (to be implemented)
# def get_stock_symbols():
#     # This could be replaced with a dynamic source
#     return [('AAPL', 'Apple Inc.'), ('GOOGL', 'Alphabet Inc.'), ('MSFT', 'Microsoft Corporation')]
