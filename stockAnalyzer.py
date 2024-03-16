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

# plot stock chart
def plot_stock_chart(stock_symbol, chart_type, closing_prices):
    chart = None
    if chart_type == "1":
        chart = pygal.Bar()
    elif chart_type == "2":
        chart = pygal.Line()

    chart.title = f'{stock_symbol} Stock Prices'
    chart.x_labels = reversed([str(i) for i in range(1, len(closing_prices) + 1)])
    chart.add('Closing Price', closing_prices)

    chart.render_to_file('stock_chart.svg')
    webbrowser.open('stock_chart.svg')

# main
def main():
    stock_symbol, chart_type, time_series, start_date, end_date = get_user_input()

    try:
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
        if end_date < start_date:
            raise ValueError("End date should not be before the start date.")
    except ValueError as e:
        print("Error:", e)
        return

    closing_prices = fetch_stock_data(stock_symbol, time_series, start_date, end_date)
    plot_stock_chart(stock_symbol, chart_type, closing_prices)

if __name__ == "__main__":
    main()