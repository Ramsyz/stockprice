import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple stock Price App

Shows are the stock **closing price** and **volume** of Nike!

""")
# tickersymbol(stock) of Amazon
tickerSymbol = 'NKE'
# Data for Amazon
tickerData = yf.Ticker(tickerSymbol)
# Historical Prices of Amazon tickerData
tickerdf = tickerData.history(period='Id', start='2019-9-30', end='2020-9-30')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerdf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerdf.Volume)
