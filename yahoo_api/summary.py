from bs4 import BeautifulSoup
import json
from .requester import get_soup, get_quote_type


def get_summary(ticker):
    """
    Get basic information about asset by scraping data from 'Summary' web page
    """
    dictionary = {}
    dictionary['Ticker'] = ticker

    # Send request to the web site
    url = f"https://finance.yahoo.com/quote/{ticker}"
    soup = get_soup(url)

    # Get Name
    string = soup.find("h1", {'class':'D(ib) Fz(18px)'}).text.strip()
    dictionary['Name'] = string[:string.index(" (")]
    
    # Get Currency & Quote type
    data_config = soup.find('div',{'id':'smartDaConfig'})
    config = json.loads(data_config['data-smart-da-config'])
    dictionary['Quote Type'] = config['dynamicData']['FIN_QUOTE_TYPE']
    dictionary['Quote Currency'] = config['dynamicData']['FIN_CURRENCY_TYPE']
    
    # Get summary's table info
    summary = soup.find('div',{'id': 'quote-summary'})
    index = summary.find_all('td',{'class' : 'C($primaryColor) W(51%)'})
    index = [string.text for string in index]
    value = summary.find_all('td',{'class' : 'Ta(end) Fw(600) Lh(14px)'})
    value = [string.text for string in value]
    for v, i in zip(value, index): dictionary[i] = v

    return dictionary