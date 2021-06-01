# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:29:22 2021

@author: Ditiro
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import streamlit as st

driver = webdriver.Chrome('/Users/Ditiro/Downloads/chromedriver.exe')
driver.get("https://www.statsbots.org.bw/motor-vehicle-accident-trend-transport-sector")
driver.implicitly_wait(15)

data = driver.find_elements_by_xpath('//*[contains(@class, "highcharts-axis-labels highcharts-xaxis-labels")]')
year_stats = []
for p in range(len(data)):
    year_stats.append(data[p].text)

stringYears = '2005\n2006\n2007\n2008\n2009\n2010\n2011\n2012\n2013\n2014'
stringYears.replace('\n',',')
yeaList = stringYears.split()

data = driver.find_elements_by_xpath('//*[contains(@class, "highcharts-data-labels highcharts-series-0")]')
year_stats = []
for p in range(len(data)):
    year_stats.append(data[p].text)

stringStats = '17 522\n17 035\n19 487\n20 415\n20 000\n18 978\n18 001\n17 527\n17 062\n16 641'
stringStats.replace('\n',',')
FinalStringStats = '17522,17035,19487,20415,20000,18978,18001,17527,17062,16641'
FStats = FinalStringStats.split(',')
type(FStats)


data_tuples = list(zip(yeaList,FStats))
df= pd.DataFrame(data_tuples, columns=['Year','No. of Accidents'])




    
st.write("""
# Botswana Accidents Trends
""")

st.sidebar.title("Interact with the dashboard")
accidata = st.button("Display Accident Data")
if accidata:
    st.write(df)

st.sidebar.markdown("Select the Charts/Plots accordingly:")

