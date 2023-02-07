from bs4 import BeautifulSoup
from .requester import get_soup, get_quote_type
import json

def get_statistics(ticker):
    """
    Get infos from statistics web page
    Works only with equity
    """
    # Initialization
    url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    soup = get_soup(url)
    QuoteType = get_quote_type(soup)
    
    # Get Currency
    data_config = soup.find('div',{'id':'smartDaConfig'})
    config = json.loads(data_config['data-smart-da-config'])
    
    if QuoteType == 'EQUITY':
        # Get infos from tables
        tables = soup.find_all('table',{'class':'W(100%) Bdcl(c)'})
        values = [[value.text for value in row] for row in [table.find_all('td') for table in tables]]
        texts = [item for sublist in values for item in sublist]
        dictionary = delister(texts)
        
        return dictionary
    
    else:
        return 'Statistics web page not found'

def delister(List):
    dictionary = {}
    for n, item in enumerate(List):
        if n % 2 ==0:
            index = item
        else:
            value = item
        if n % 2 == 0:
            pass
        else:
            dictionary[index] = value
    return dictionary
