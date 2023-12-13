# yahoo_api
A python library to scrape Yahoo! Finance

This library enables users to independently collect financial data from Yahoo! Finance, thereby eliminating the need for third-party data providers. This allows for greater flexibility and control over the data collection process, saving valuable time and effort.

The library is designed to be as easy as possible to use. Most of the methods of this library are called like Yahoo! Finance's Webpages.

## New Feature: Stock Data Web Page
The latest update includes a web page feature that allows users to view stock data directly through a web interface. This feature is built using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Setting up the Django Project
To set up the project, follow these steps:
1. Ensure you have Python and Django installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run `python manage.py migrate` to set up the database.
5. Start the server with `python manage.py runserver`.

### Running the Server
Once the project is set up, you can run the Django server with the following command:
```
python manage.py runserver
```
This will start the server on `http://127.0.0.1:8000/` by default.

### Navigating to the Stock Data Web Page
After starting the server, open your web browser and go to `http://127.0.0.1:8000/stocks` to access the stock data web page.

You can support my work here: https://www.buymeacoffee.com/matteobernard
