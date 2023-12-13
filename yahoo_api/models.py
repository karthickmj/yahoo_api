from django.db import models


class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10, unique=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker_symbol
