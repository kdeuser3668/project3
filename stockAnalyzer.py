# stockAnalyzer.py

from datetime import datetime
import requests
import pygal
import webbrowser

# get user input
def get_user_input():
    stock_symbol = input("Enter the stock symbol: ").upper()
    chart_type = input("Enter 1 for Bar chart, 2 for Line chart: ")
    time_series = input("Enter time series (1: Intraday, 2: Daily, 3: Weekly, 4: Monthly): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date in YYYY-MM-DD format: ")

    return stock_symbol, chart_type, time_series, start_date, end_date

# get stock data
def get_stock_data(stock_symbol, time_series, start_date, end_date):
    api_key = '11R1UGRP10LKEMDQ'
    url = f'https://www.alphavantage.co/query?function={time_series}&symbol={stock_symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    time_series_output = None

    if time_series == "1":
        time_series_output = "Time Series (5min)"
    elif time_series == "2":
        time_series_output = "Time Series (Daily)"
    elif time_series == "3":
        time_series_output = "Weekly Time Series"
    elif time_series == "4":
        time_series_output = "Monthly Time Series"

    closing_prices = []

    for date, values in data[time_series_output].items():
        closing_prices.append(float(values['4. close']))

    return closing_prices