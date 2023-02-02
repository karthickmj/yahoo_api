from .summary import get_summary
from .history import get_history, get_dividend
from .finance import get_financials
from .profile import get_profile
from .holders import get_holders
from .statistics import get_statistics

class ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def history(self, period, continuous = False):
        return get_history(self.ticker, period, continuous)

    def dividend(self, period):
        return get_dividend(self.ticker, period)

    def summary(self):
        return get_summary(self.ticker)
    
    def financials(self, statement):
        return get_financials(self.ticker, statement)

    def profile(self):
        return get_profile(self.ticker)

    def holders(self):
            return get_holders(self.ticker)

    def statistics(self):
            return get_statistics(self.ticker)
