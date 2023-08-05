#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:45:02 2023

@author: mohan
"""

import pandas as pd
import asyncio
import yfinance as yf
import websockets
import json
import threading

# Function to fetch live stock data using yfinance
def fetch_live_stock_data(ticker):
    return yf.download(ticker, period="1d", interval="1m")

# Function to store live stock data in the DataFrame
def store_live_stock_data_to_dataframe():
    ticker = "ITC"  # Replace this with your desired stock symbol
    df = fetch_live_stock_data(ticker)
    print("Initial DataFrame:")
    print(df)

    # Function to update DataFrame with live data
    def update_dataframe(data):
        nonlocal df
        live_data = json.loads(data)
        new_data = pd.DataFrame([live_data])
        new_data.set_index("timestamp", inplace=True)
        df = pd.concat([df, new_data], axis=0, sort=False)
        print("Updated DataFrame:")
        print(df)

    async def handle_socket():
        uri = "wss://your-websocket-server-url"  # Replace this with the actual WebSocket server URL
        async with websockets.connect(uri) as websocket:
            while True:
                data = await websocket.recv()
                threading.Thread(target=update_dataframe, args=(data,)).start()

    # Start the WebSocket connection and continuously update the DataFrame
    asyncio.get_event_loop().run_until_complete(handle_socket())


if __name__ == "__main__":
    store_live_stock_data_to_dataframe()
