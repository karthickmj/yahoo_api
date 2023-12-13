# yahoo_api
A python library to scrape Yahoo! Finance

This library enables users to independently collect financial data from Yahoo! Finance, thereby eliminating the need for third-party data providers. This allows for greater flexibility and control over the data collection process, saving valuable time and effort.

I want this library easy as possible to use. Most of methods of this library are called like Yahoo! Finance's Webpages.

You can support my work here: https://www.buymeacoffee.com/matteobernard

## Web Page Feature

The yahoo_api library now includes a web page feature that allows users to interact with the stock data through a web interface. To use this feature, follow the instructions below:

### Running the Django Server

1. Navigate to the project directory where `manage.py` is located.
2. Run the Django server using the following command:

   ```
   python manage.py runserver
   ```

   This will start the server on the default port 8000. You can access the server at `http://127.0.0.1:8000/`.

### Accessing the Stock Data Page

1. Once the server is running, open a web browser.
2. Go to `http://127.0.0.1:8000/stocks` to access the stock data page.

### Selecting a Stock Ticker

1. On the stock data page, you will find an input field to enter a stock ticker symbol.
2. Enter the desired stock ticker symbol and submit.
3. The page will display the financial data for the selected stock ticker.

Please note that the web page feature is an additional tool provided by the yahoo_api library and does not replace the core functionality of the library which is to scrape financial data programmatically.