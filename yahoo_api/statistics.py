from bs4 import BeautifulSoup
from .requester import get_soup, get_quote_type
import json

def get_statistics(ticker):
    """
    Get infos from statistics web page
    Works only with equity
    """
    # Initialization
    dictionary = {}
    url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}'
    soup = get_soup(url)
    QuoteType = get_quote_type(soup)
    
    # Get Currency
    data_config = soup.find('div',{'id':'smartDaConfig'})
    config = json.loads(data_config['data-smart-da-config'])
    dictionary['Quote Currency'] = config['dynamicData']['FIN_CURRENCY_TYPE']
    
    if QuoteType == 'EQUITY':
        # Get infos from tables
        index = soup.find_all('td',{'class':'Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px)'})
        value = soup.find_all('td',{'class':'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})
        index = [i.text for i in index]
        value = [v.text for v in value]
        for v, i in zip(value, index): dictionary[i] = v
        
        return dictionary
    
    else:
        return 'Statistics web page not found'