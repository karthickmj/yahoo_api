from django import forms


class StockSelectForm(forms.Form):
    STOCK_CHOICES = [
        ('AAPL', 'Apple Inc.'),
        ('GOOGL', 'Alphabet Inc.'),
        ('MSFT', 'Microsoft Corporation'),
        ('AMZN', 'Amazon.com, Inc.'),
        ('FB', 'Facebook, Inc.'),
        # Add more stock choices here
    ]

    ticker = forms.ChoiceField(choices=STOCK_CHOICES, label='Select Stock Ticker')
