#activate if it's not already
#\env\Scripts\activate\
#deactivate when done - deactivate

import csv
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, types
#connect to the csv file and build the DataFrame
#data = pd.read_csv(r'D:\projects\TSN Mining\TSN Mining\ores3.csv')
#df = pd.DataFrame(data, columns=['rawmineral','rawvalue', 'refinedmineral', 'refinedvalue','resistance', 'oes'])
#print(df)

#create connection
engine = create_engine('mysql://root:@localhost/tsn_mining')

#connect to csv
df = pd.read_csv("D:\projects\TSN Mining\TSN Mining\ores3.csv",sep=',',quotechar='\'',encoding='utf8')
#upload to database
df.to_sql('mineral_info',con=engine,index=False,if_exists='replace')
