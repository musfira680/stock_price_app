import yfinance as yf
import streamlit as st
import pandas as pd

st.title('Simple Stock Price App')


stock = st.text_input('Enter the ticker symbol which company stock price you want to see:')

if stock:
    st.text(f"Shown are the stock closing price and volume of {stock}")
    
    tickersymbol = stock

   
    tickerData = yf.Ticker(tickersymbol)

    
    tickerof = tickerData.history(start='2015-07-11', end='2025-07-11')

    st.subheader('Closing Price')
    st.line_chart(tickerof['Close'])
    st.subheader('Volume Price')
    st.line_chart(tickerof['Volume'])
