#don't forget to activate virtual #!/usr/bin/env python
#\env\Scripts\activate\
#deactivate when done - deactivate


#import webdriver
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://sc-trade.tools/ores/MISC%20Prospector%20or%20Argo%20Mole'

#initiating the webdriver with parameters
driver = webdriver.Chrome('D:/Python/Scripts/chromedriver')
driver.get(url)

#time to load the webpage
time.sleep(5)
html = driver.page_source

#finds the table and creates the list
soup = BeautifulSoup(html, "html.parser")
ore_table = soup.find_all('table')

#create the dataframe object
#delete challenge rating and sub-chunk
#remove the currency symbol and UEC from  Ore/Refined Value
df = pd.read_html(str(ore_table))[0]
del df['Challenge rating'],df['Sub-chunk purity']
df['Ore value'] = df['Ore value'].replace({' UEC':'', '¤':''}, regex=True)
df['Refined value'] = df['Refined value'].replace({' UEC':'', '¤':''}, regex=True)

#rename columns
df.index.name='id'
df.columns=['rawmineral','rawvalue','refinedmineral','refinedvalue','resistance','oes']

#output to csv
df.to_csv(r'D:\projects\TSN Mining\TSN Mining\ores3.csv', index=True, header=True)
print(df)

#close the webdriver
driver.close()
