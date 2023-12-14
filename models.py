from django.db import models
from django.contrib.postgres.fields import JSONField


class Stock(models.Model):
    ticker_symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    market_change = models.DecimalField(max_digits=10, decimal_places=2)
    market_change_percent = models.DecimalField(max_digits=10, decimal_places=2)
    financial_highlights = JSONField()

    def __str__(self):
        return f'{self.name} ({self.ticker_symbol})'