# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 12:04:28 2023

@author: USER
"""

import streamlit as st 
import telebot
import pandas_ta as ta
import pandas as pd
from urllib.request import urlopen
import certifi
import json
import datetime
import time

FMP = apikey="e3e1ef68f4575bca8a430996a4e11ed1"
telegram = "5936010971:AAGao0RYG_gU28OfnpCIvCl_irCeHjU-muQ"
bot = telebot.TeleBot(telegram)


symbol = "EURUSD"
signal = st.text_input("target price")
signal = float(signal)
alert_dt = datetime.datetime(1970, 1, 1, 0, 0, 0)
alert = 3
numbers = st.empty()
counter = 0

while True:
    time.sleep(10)
    response = urlopen(f"https://financialmodelingprep.com/api/v3/historical-chart/1min/{symbol}?apikey={FMP}")
    price_list = response.read().decode("utf-8")
    price_list = json.loads(price_list)
    price_list =pd.DataFrame(price_list)
    last_price = price_list.at[0,"close"]
    date = price_list.at[0,"date"]
    crossover = 1 if signal > last_price else 0
    counter = counter +1 
    with numbers.container():
        st.write(f"Last price: {last_price}")
        st.write(f"Date Time: {date}")
        st.write(f"crossover: {crossover}")
        st.write(f"alert: {alert}")
        


    if crossover == 1 and alert >0:
        message = f'请注意：{symbol}价格向上穿越 {signal}啦😉'
        bot.send_message(1012061905, message)
        alert_once = True
        alert -= 1