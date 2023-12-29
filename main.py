import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Access the API key using the os module
api_key = os.getenv("API_KEY")

print("API Key:", api_key)

st.title('Stock Dashboard')
default_ticker = 'AAPL'
ticker = st.sidebar.text_input('Stock', default_ticker)

# Set default start and end dates
default_start_date = datetime(2023, 1, 1)
default_end_date = datetime(2023, 4, 1)

start_date = st.sidebar.date_input('Start Date', value=default_start_date)
end_date = st.sidebar.date_input('End Date', value=default_end_date)

data = yf.download(ticker, start=start_date, end=end_date)

# Check if the DataFrame is empty before plotting
if not data.empty:
    fig = px.line(data, x=data.index, y='Adj Close', title=ticker)
    st.plotly_chart(fig)
else:
    st.warning(f"No data available for {ticker} in the selected date range.")

pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Price Movements')
    dataCopy = data
    dataCopy['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    dataCopy.dropna(inplace = True)
    st.write(data)
    annual_return = dataCopy['% Change'].mean()*252*100
    st.write("Annual Return is ", annual_return, '%')
    stdev = np.std(dataCopy['% Change'])*np.sqrt(252)
    st.write("Standard Deviation is ", stdev*100, '%')
    st.write('Risk Adj. Return is ',annual_return/(stdev*100))


from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    fd = FundamentalData(api_key, output_format = 'pandas')
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)

from stocknews import StockNews
with news:
    st.header(f'Top 10 {ticker} News')
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'Article {i + 1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
    
