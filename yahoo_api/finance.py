import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from .requester import get_soup, get_quote_type

def get_financials(ticker, statement):
    
    # Check the financials statement asked
    statement = ('financials' if statement == 'income-statement' else statement)
    num_columns = (4 if statement == 'balance-sheet' else 5)
            
    # Send request to Yahoo! Finance
    url = f'https://finance.yahoo.com/quote/{ticker}/{statement}?p={ticker}'
    soup = get_soup(url)
    QuoteType = get_quote_type(soup)
    
    # Check if quotype is equity
    if QuoteType == 'EQUITY':
        # Scrape table's data, index and columns
        table = soup.find("div",attrs={"class":'M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)'})
        columns = [column.get_text() for column in soup.find("div",attrs={"class":'D(tbr) C($primaryColor)'})]
        index = [index.get_text() for index in table.find_all('div', attrs={'class': 'Va(m)'})]
        data = [data.get_text() for data in table.find_all('div', attrs={'data-test': 'fin-col'})]

        # Clean data
        data = [float(value.replace(",", "")) if value != '-' else '-' for value in data]  
        data = np.reshape(np.array(data),(len(index),len(columns)-1))

        # Clean table 
        df = pd.DataFrame(data=data, index=index, columns=columns[1:])
        if len(df.columns) == 5:
            df = df.drop('ttm', axis=1)
        else:
            date = df.iloc[:,1].name
            last_year = date[-4:]
            ttm_date = date.replace(
                last_year,
                str(int(last_year)+1)
            )
            df = df.rename(columns={'ttm':ttm_date})

        return df
    else:
        return 'Financials web page not found'
