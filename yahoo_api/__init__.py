from .info import get_info
from .history import get_history

class ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def history(self, period, continuous = False):
        return get_history(self.ticker, period, continuous)
    
    def info(self):
        return get_info(self.ticker)
    
