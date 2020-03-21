import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import datetime

st.write('Fahrräder')
city = st.selectbox(
	'Select city',
	('Karlsruhe', 'Freiburg_Wiwilibruecke', 'Freiburg_Hindenburgstr'))
	
start = st.date_input('start', value=datetime.date(2020, 1, 1))
end = st.date_input('end') # no value = today

if (start>end):
	tmp = start
	start = end
	end = tmp

file = 'bikecount_'+city+'_2013-2020.json'
with open(file,'r') as f:
	data = json.load(f)

tmp = []



for d in data[:-2]:
	tmp.append((d[0],d[1]))
df = pd.DataFrame(tmp,columns=['date','bikecount'])
df['date']=df['date'].astype('datetime64[ns]')
df['bikecount']=df['bikecount'].astype(float)

#st.write(df.dtypes)
#st.dataframe(df)

df_filtered = df[( df['date'] > pd.to_datetime(start) ) & ( df['date'] < pd.to_datetime(end) ) ]

fig=plt.figure()
plt.plot(df_filtered['date'],df_filtered['bikecount'])
plt.title('Bikecount in '+city.replace('_', ' '))
plt.xlabel('Datum')
plt.ylabel('Fahrräder')
plt.show()
st.plotly_chart(fig)
