import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import random
import io
import re
from datetime import datetime, date, timedelta

class ticker:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_stock_data(self):
        summary_data = self.summary()
        stats_data = self.statistics()
        return {'Summary': summary_data, 'Statistics': stats_data}

    def summary(self):
        ticker = self.ticker

        dictionary = {}
        dictionary['Ticker'] = ticker

        url = f"https://finance.yahoo.com/quote/{ticker}"
        response = requests.get(url, headers={'User-Agent': 'Safari/537.36'}, timeout=random.randint(7, 14))
        soup = BeautifulSoup(response.text, 'html.parser')

        dictionary['Full Name'] = soup.title.text[:soup.title.text.index(" (")]
        dictionary['Market Price'] = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        dictionary['Currency'] = soup.find('div', {'class': 'C($tertiaryColor) Fz(12px)'}).text.rsplit(' ', 1)[-1]
        dictionary['Market Change'] = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)', 'data-field': 'regularMarketChange'}).text.replace('+', '')
        dictionary['Market Change Percent'] = re.sub(r'[+()%]', '', soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)', 'data-field': 'regularMarketChangePercent'}).text)

        table = soup.find('div', {'id': 'quote-summary'})
        index = table.find_all('td', {'class': 'C($primaryColor) W(51%)'})
        value = table.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})
        for i, v in zip(index, value):
            dictionary[i.text] = v.text
        return dictionary

    def statistics(self):
        ticker = self.ticker

        dictionary = {}

        url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics'
        response = requests.get(url, headers={'User-Agent': 'Safari/537.36'}, timeout=random.randint(7, 14))
        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table', {'class': 'W(100%) Bdcl(c)'})
        values = [[value.text for value in row] for row in [table.find_all('td') for table in tables]]
        texts = [item for sublist in values for item in sublist]
        for n, item in enumerate(texts):
            if n % 2 == 0:
                index = item
            else:
                value = item
            if n % 2 == 0:
                pass
            else:
                dictionary[index] = value

        return dictionary

    # The rest of the methods (history, profile, financials, holders) remain unchanged
