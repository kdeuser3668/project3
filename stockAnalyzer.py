# stockAnalyzer.py

from datetime import datetime
import requests
import pygal
import webbrowser

def get_user_input():
    stock_symbol = input("Enter the stock symbol: ").upper()
    chart_type = input("Enter 1 for Bar chart, 2 for Line chart: ")
    time_series = input("Enter time series (1: Intraday, 2: Daily, 3: Weekly, 4: Monthly): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date in YYYY-MM-DD format: ")

    return stock_symbol, chart_type, time_series, start_date, end_date
