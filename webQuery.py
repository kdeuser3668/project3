#webQuery.py
import requests
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Get user input
stock_symbol = input("Enter the stock symbol: ")

# Get user input for chart type
while True:
    print("\nChart Types\n----------------\n1) Bar\n2) Line\n")
    chart_type = input("Enter 1 for Bar chart, 2 for Line chart: ")
    if chart_type in ["1", "2"]:
        break
    else:
        print("Invalid input\n")

# Get user input for time series
while True:
    print("\nTime Series\n----------------\n1) Intraday\n2) Daily\n3) Weekly\n4) Monthly\n")
    time_series = input("Enter time series (1, 2, 3, 4): ")
    if time_series in ["1", "2", "3", "4"]:
        break
    else:
        print("Invalid Input\n")

# Get user input for start date
while True:
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.\n")

# Get user input for end date
while True:
    end_date = input("Enter the end date in YYYY-MM-DD format: ")
    try:
        datetime.strptime(end_date, "%Y-%m-%d")
        if end_date >= start_date:
            break
        else:
            print("The end date should not be before the begin date.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.\n")

# Send user input to Alpha Vantage API
base_url = "https://www.alphavantage.co/query?"
api_key = "11R1UGRP10LKEMDQ" 

# Construct parameters for API request
params = {
    "function": "TIME_SERIES_DAILY",  # Adjust the function based on time_series selection
    "symbol": stock_symbol,
    "apikey": api_key,
}

# Make API request
response = requests.get(base_url, params=params)

# Check if API request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract and process data from the Alpha Vantage API response
    time_series_data = data.get("Time Series (Daily)")
    if time_series_data is None:
        print("No data available for the selected stock symbol.")
        exit(1)

    # Extract dates and closing prices from API response
    dates = list(time_series_data.keys())
    prices = [float(time_series_data[date]["4. close"]) for date in dates]

    # Visualize the data using matplotlib
    plt.figure(figsize=(10, 6))
    if chart_type == "1":
        plt.bar(dates, prices, label="Stock Price", color="g")
    else:
        plt.plot(dates, prices, label="Stock Price", color="b")

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"Stock Price Chart ({'Bar' if chart_type == '1' else 'Line'})")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

else:
    print("Failed to retrieve data from Alpha Vantage API.")

