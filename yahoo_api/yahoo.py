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
        """
        Initialize the Ticker object with the provided stock ticker symbol.

        Parameters
        ----------
        ticker : str
            The stock ticker symbol for the desired company.
        """
        self.ticker = ticker
        
    def summary(self):
        """
        Retrieve summary data from the 'Summary' web page for equity instruments.

        Returns
        -------
        dict
            A dictionary containing summary information about the company.

        Notes
        -----
        This function is designed to work specifically with equity instruments.

        Examples
        --------
        >>> summary_data = yahoo.ticker('AI.PA').summary()
        >>> print(summary_data)
        """
        ticker = self.ticker

        dictionary = {}
        dictionary['Ticker'] = ticker

        # Send request to the web site
        url = f"https://finance.yahoo.com/quote/{ticker}"
        response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= random.randint(7, 14))
        soup = BeautifulSoup(response.text,'html.parser')

        # Get additional data about product
        dictionary['Full Name'] = soup.title.text[:soup.title.text.index(" (")]
        dictionary['Market Price'] = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        dictionary['Currency'] = soup.find('div', {'class':'C($tertiaryColor) Fz(12px)'}).text.rsplit(' ', 1)[-1]
        dictionary['Market Change'] = soup.find('fin-streamer',{'class':'Fw(500) Pstart(8px) Fz(24px)', 'data-field':'regularMarketChange'}).text.replace('+','')
        dictionary['Market Change Percent'] = re.sub(r'[+()%]', '', soup.find('fin-streamer',{'class':'Fw(500) Pstart(8px) Fz(24px)', 'data-field':'regularMarketChangePercent'}).text)

        # Get content of summary table
        table = soup.find('div',{'id':'quote-summary'})
        index = table.find_all('td',{'class':'C($primaryColor) W(51%)'})
        value = table.find_all('td',{'class':'Ta(end) Fw(600) Lh(14px)'})
        for i, v in zip(index, value):
            dictionary[i.text] = v.text
        return dictionary
    
    def statistics(self):
        """
        Retrieve key statistics data from the 'statistics' web page for equity instruments.

        Returns
        -------
        dict
            A dictionary containing key statistics information.

        Notes
        -----
        This function is designed to work specifically with equity instruments.

        Examples
        --------
        >>> stats_data = yahoo.ticker('ACA.PA').statistics()
        >>> print(stats_data)
        """
        
        # Initialization
        ticker = self.ticker
        url = f'https://finance.yahoo.com/quote/{ticker}/key-statistics'
        response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= random.randint(7, 14))
        soup = BeautifulSoup(response.text,'html.parser')
        
        # Get infos from tables
        dictionary = {}
        tables = soup.find_all('table',{'class':'W(100%) Bdcl(c)'})
        values = [[value.text for value in row] for row in [table.find_all('td') for table in tables]]
        texts = [item for sublist in values for item in sublist]
        for n, item in enumerate(texts):
            if n % 2 ==0:
                index = item
            else:
                value = item
            if n % 2 == 0:
                pass
            else:
                dictionary[index] = value
        
        return dictionary
        
    def history(self, period='1y', frequency='D', kind='history'):
        """
        Retrieve historical financial data from the 'history' web page.

        Parameters
        ----------
        period : str, optional
            Specifies the time period for historical data.
            Should be one of ['max', '10y', '5y', '1y', '6m', '1m', '5d', '1d'].
            Default is '1y'.

        frequency : str, optional
            Specifies the frequency of historical data.
            Should be one of ['D', 'M', 'W'] for daily, monthly, or weekly data.
            Default is 'D' (daily).

        kind : str, optional
            Specifies the type of historical data to retrieve.
            Should be one of ['history', 'dividend', 'split', 'gain'].
            Default is 'history'.

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame containing historical financial data.

        Notes
        -----
        This function is designed to work specifically with equity instruments.

        Examples
        --------
        >>> historical_data = yahoo.ticker('MC.PA').history(period='5y', frequency='M', kind='history')
        >>> print(historical_data)
        """

        # Get type of history asked
        eventsDict = {
            'history':'history',
            'dividend': 'div',
            'split': 'split',
            'gain':'capitalGain',
        }
        events= eventsDict[kind]

        # Get interval of the asked history
        freqDict = {
            'D':'1d',
            'W':'1wk',
            'M':'1mo'
        }
        interval = freqDict[frequency]
        
        # Use datetime to define length of asked history
        timeDict = {
            '10y': 3650,
            '5y': 1825,
            '1y': 365,
            '6m': 182,
            '1m': 30,
            '5d': 5,
            '1d': 1
        }        
        if period == 'max': 
            period1 = '0'
        else:
            period1 = str(int((datetime.now()-timedelta(days=timeDict[period])).timestamp()))
        period2 = str(int(datetime.now().timestamp()))
        
        # Get response from Yahoo html
        ticker = self.ticker
        url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events={events}&includeAdjustedClose=true'
        response = requests.get(
            url,
            headers={'User-Agent': 'Safari/537.36'},
            timeout= random.randint(7, 14)
        )
        
        # Get DataFrame from response
        csv_file = io.StringIO(response.text)
        df = pd.read_csv(csv_file, index_col = 'Date')
        
        # clean DataFrame
        df.index = pd.to_datetime(df.index)
        if events != 'split' and events != 'gain':
            df = df.apply(pd.to_numeric, errors='coerce')
        if events == 'history':
            df['Volume'].fillna(0, inplace=True)
            df.dropna(subset=['Open'], inplace=True)       
        return df
    
    def profile(self, description= False):
        """"
        Retrieve data from the 'profile' web page for equity instruments.

        Parameters
        ----------
        description : bool, optional
            If True, return the description of the company along with other profile information.
            Default is False.

        Returns
        -------
        dict or tuple
            If `description` is True, returns a tuple containing a dictionary with profile information
            and the company description as a string. If False, returns a dictionary with profile information.

        Notes
        -----
        This function is designed to work specifically with equity instruments.

        Examples
        --------
        >>> profile_data = yahoo.ticker('ORA.PA').profile(description=True)
        >>> print(profile_data)
        """

        # Get soup from Yahoo html
        ticker = self.ticker
        url = f'https://finance.yahoo.com/quote/{ticker}/profile?p={ticker}'
        response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= random.randint(7, 14))
        soup = BeautifulSoup(response.text,'html.parser')

        # Get full name
        dictionary = {}
        string = soup.find('h3',{'class':'Fz(m) Mb(10px)'}).text
        dictionary['Full Name'] = string

        # Get contact info
        table = soup.find('p',{'class':'D(ib) W(47.727%) Pend(40px)'})
        value = table.contents
        value[6] = value[6].text
        value[8] = value[8].text
        [value.pop(br) for br in range(1,5)]
        index = ['Road', 'City', 'Country', 'Tel Number', 'WebSite']
        for v, i in zip(value, index): dictionary[i] = v

         # Get sector's info
        tags = soup.find_all("p", {'class':'D(ib) Va(t)'})
        table = [item.text for item in tags[0].contents if item.text != ':\xa0']
        index = [table[item] for item in [0,3,6]]
        value = [table[item] for item in [1,4,7]]
        for v, i in zip(value, index): dictionary[i] = v

        if description is True:
            # get description
            description_str = soup.find('p',{'class':'Mt(15px) Lh(1.6)'}).text
            return dictionary, description_str
        else:
            return dictionary
    
    def financials(self, statement, expand_all=False):
        """
        Retrieve financial data from the 'financials' web page for equity instruments.

        Parameters
        ----------
        statement : str
            Specifies the financial statement type to retrieve. 
            Should be one of ['income-statement', 'cash-flow', 'balance-sheet'].

        expand_all : bool, optional
            If True, use Selenium to scrape the web page for the complete financial statement.
            Default is False.

        Returns
        -------
        pandas.DataFrame
            A pandas DataFrame containing the financial data.

        Notes
        -----
        This function is designed to work specifically with equity instruments.

        Examples
        --------
        >>> data = yahoo.ticker('DG.PA').financials('income-statement', expand_all=True)
        >>> print(data)
        """

        # Check the financials statement asked
        ticker = self.ticker
        statement = ('financials' if statement == 'income-statement' else statement)
        num_columns = (4 if statement == 'balance-sheet' else 5)
        
        if expand_all is True:
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service as ChromeService
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            from selenium.webdriver.common.by import By

            # Initialize Selenium
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--user-data-dir=/Users/matteobernard/Library/Application Support/Google/Chrome/")
            path = "/Users/matteobernard/Documents/Data Science/Data Mining/chorme driver/chromedriver"
            driver = webdriver.Chrome(executable_path=path, options=options)

            url = f'https://finance.yahoo.com/quote/{ticker}/{statement}'
            driver.get(url)

            # Accept cookies
            cookies_xpath = '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button[2]'
            try: 
                driver.find_element(By.XPATH, cookies_xpath).click() 
            except: 
                pass

            # Click on "expand all" button to get all data available
            span_button = '#Col1-1-Financials-Proxy > section > div.Mb\(10px\) > button > div > span'
            if driver.find_element(By.CSS_SELECTOR,span_button).text == 'Expand All':
                button_selector = '#Col1-1-Financials-Proxy > section > div.Mb\(10px\) > button'
                driver.find_element(By.CSS_SELECTOR,button_selector).click()

            # Get HTML page from Selenium driver
            html = driver.page_source
            soup = BeautifulSoup(html, features="lxml")
        
        else:
            # Send request to Yahoo! Finance
            url = f'https://finance.yahoo.com/quote/{ticker}/{statement}'
            response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= random.randint(7, 14))
            soup = BeautifulSoup(response.text,'html.parser')

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
        df.columns = pd.to_datetime(df.columns)
        return df
    
    def holders(self):
        # Get soup from Yahoo html
        ticker = self.ticker
        url = f'https://finance.yahoo.com/quote/{ticker}/holders?p={ticker}'
        response = requests.get(url,headers= {'User-Agent': 'Safari/537.36'},timeout= random.randint(7, 14))
        soup = BeautifulSoup(response.text,'html.parser')

        # Get Major Holders
        dictionary = {}
        table = soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'})
        value = table.find_all('td',{'class':'Py(10px) Va(m) Fw(600) W(15%)'})
        value = [string.text for string in value]
        index = table.find_all('td',{'class':'Py(10px) Ta(start) Va(m)'})
        index = [string.text for string in index]
        for v, i in zip(value, index): 
            dictionary[i] = v
        major_holders = pd.DataFrame(data=dictionary.values(), index=dictionary.keys(), columns=['% Out'])

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

        return major_holders, institutional, mutual_fund