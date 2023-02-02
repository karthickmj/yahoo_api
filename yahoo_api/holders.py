from bs4 import BeautifulSoup
from .requester import get_soup, get_quote_type
import pandas as pd

def get_holders(ticker):
    """
    Get infos about equity's holders from the 'Holders' web page
    Works only with equity
    Return a dictionary and 2 dataframe that respectively 
    contains info about Major Holders, Top Institutional Holders, Top Mutual Fund Holders
    """
    dictionary = {}
    url = f'https://finance.yahoo.com/quote/{ticker}/holders?p={ticker}'
    soup = get_soup(url)
    QuoteType = get_quote_type(soup)
    
    if QuoteType == 'EQUITY':
        # Get Major Holders
        table = soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'})
        value = table.find_all('td',{'class':'Py(10px) Va(m) Fw(600) W(15%)'})
        value = [string.text for string in value]
        index = table.find_all('td',{'class':'Py(10px) Ta(start) Va(m)'})
        index = [string.text for string in index]
        for v, i in zip(value, index): dictionary[i] = v

        # Get Top Institutional Holders
        table = soup.find('div',{'class':'Mt(25px) Ovx(a) W(100%)'})
        head = [head.text for head in table.find('tr',{'class':'C($tertiaryColor) Fz(xs)'})]
        rows = table.find_all('tr',{'class':'BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)'})
        rows = [[string.text for string in row] for row in rows]
        institutional = pd.DataFrame(data=rows, columns=head)
        
        # Get Top Mutual Fund Holders
        table = soup.find_all('div',{'class':'Mt(25px) Ovx(a) W(100%)'})
        head = [head.text for head in table[1].find('tr',{'class':'C($tertiaryColor) Fz(xs)'})]
        rows = table[1].find_all('tr',{'class':'BdT Bdc($seperatorColor) Bgc($hoverBgColor):h Whs(nw) H(36px)'})
        rows = [[string.text for string in row] for row in rows]
        mutual_fund = pd.DataFrame(data=rows, columns=head)
    
        return dictionary, institutional, mutual_fund
    
    else:
        return 'Holders web page not found'
