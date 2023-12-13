from django import forms


class StockSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # Assuming 'choices' is passed as a keyword argument
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['ticker_symbol'] = forms.ChoiceField(choices=choices)
