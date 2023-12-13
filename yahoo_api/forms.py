from django import forms
from .models import Stock


class StockSelectionForm(forms.Form):
    ticker = forms.ModelChoiceField(queryset=Stock.objects.all(), empty_label='Select Stock')
