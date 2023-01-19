from .info import get_info
from .history import get_history
from .history import get_dividend
from .finance import get_financials

class ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def history(self, period, continuous = False):
        return get_history(self.ticker, period, continuous)

    def dividend(self, period):
        return get_dividend(self.ticker, period)

    def info(self):
        return get_info(self.ticker)
    
    def financial(self, statement):
        return get_financials(self.ticker, statement)
