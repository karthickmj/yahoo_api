from bs4 import BeautifulSoup
from .requester import get_soup, get_quote_type

def get_profile(ticker):
    dictionary = {}
    # Send request to the web site
    url = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
    soup = get_soup(url)
    QuoteType = get_quote_type(soup)
    
    if QuoteType == 'EQUITY':
        # Get full name
        string = soup.find('h3',{'class':'Fz(m) Mb(10px)'}).text
        dictionary['FullName'] = string
    
        # Get contact info
        table = soup.find('p',{'class':'D(ib) W(47.727%) Pend(40px)'})
        value = table.contents
        value[6] = value[6].text
        value[8] = value[8].text
        [value.pop(br) for br in range(1,5)]
        index = ['Road', 'City', 'Country', 'TelNumber', 'WebSite']
        for v, i in zip(value, index): dictionary[i] = v

         # Get sector's info
        tags = soup.find_all("p", {'class':'D(ib) Va(t)'})
        table = [item.text for item in tags[0].contents if item.text != ':\xa0']
        index = [table[item] for item in [0,3,6]]
        value = [table[item] for item in [1,4,7]]
        for v, i in zip(value, index): dictionary[i] = v

        # get description
        description = soup.find('p',{'class':'Mt(15px) Lh(1.6)'}).text
        dictionary['Description'] = description
        
        return dictionary
    
    elif QuoteType == 'ETF':
        # Get name
        name = soup.find('h3', {'class': 'Mb(5px) Mend(40px)'}).text
        dictionary['Name'] = name
        
        # Get Fund overview
        table = soup.find('div', {'class': 'Mb(25px)'})
        tags = table.find_all('span', {'class': 'Mend(5px) Whs(nw)'})
        index = [index.text for index in tags]
        tags = table.find_all('span', {'class': 'Fl(end)'})
        value = [value.text for value in tags]
        for v, i in zip(value, index): dictionary[i] = v
    
        return dictionary
    
    else:
        return 'Profile Web page not found'