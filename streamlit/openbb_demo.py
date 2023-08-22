import streamlit as st
import pandas as pd

from openbb_terminal.sdk import openbb

#df_daily = openbb.stocks.load(symbol = 'APG1L.VS')

st.title('Sample OpenBB Output')
st.subtitle('Balance Sheet')

balance_sheet = openbb.stocks.fa.balance("APG1L.VS", source="YahooFinance")

st.table(balance_sheet.head())

st.subtitle('Balance Sheet')
fig = openbb.stocks.candle(
    data = openbb.stocks.load(symbol = 'APG1L.VS', start_date = '2023-06-01', weekly = True, verbose = False),
    symbol = "APB Apranga - Weekly"
)

st.plotly_chart(fig)