import requests
from bs4 import BeautifulSoup
from lxml import html
import json

def get_info(ticker):
    # Send request to the web site
    url = f"https://finance.yahoo.com/quote/{ticker}"
    
    response = requests.get(
                url,
                headers= {'User-Agent': 'Safari/537.36'},
                timeout= 10
            )
    
    # Get Name
    soup = BeautifulSoup(
            response.content,
            'lxml'
        )
    string = soup.find(
        "h1", {
            'class':'D(ib) Fz(18px)'
        }
    ).text.strip()
    name = string[:string.index(" (")]
    
    # Get Currency & Quote type
    tree = html.fromstring(
        response.content
    )
    json_string = tree.xpath(
        "//div[@id='smartDaConfig']/@data-smart-da-config"
    )[0]
    data = json.loads(
        json_string
    )
    currency_type = data['dynamicData']['FIN_CURRENCY_TYPE']
    quote_type = data['dynamicData']['FIN_QUOTE_TYPE']
    return {
        'Name': name,
        'Quote': quote_type,
        'Currency': currency_type
    }