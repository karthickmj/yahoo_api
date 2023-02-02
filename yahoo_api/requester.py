import requests
from bs4 import BeautifulSoup
import json

def get_soup(url):
    """
    Get soup
    """
    response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= 10)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def get_quote_type(soup):
    """
    Get quotetype by checking response
    """
    data_config = soup.find('div',{'id':'smartDaConfig'})
    config = json.loads(data_config['data-smart-da-config'])
    QuoteType = config['dynamicData']['FIN_QUOTE_TYPE']
    return QuoteType