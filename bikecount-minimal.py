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
	


file = 'bikecount_'+city+'_2013-2020.json'
with open(file,'r') as f:
	data = json.load(f)

tmp = []



for d in data[:-2]:
	tmp.append((d[0],d[1]))
df = pd.DataFrame(tmp,columns=['date','bikecount'])
df['date']=df['date'].astype('datetime64[ns]')
df['bikecount']=df['bikecount'].astype(float)



fig=plt.figure()
plt.plot(df['date'],df['bikecount'])
plt.title('Bikecount in '+city.replace('_', ' '))
plt.xlabel('Datum')
plt.ylabel('Fahrräder')
plt.show()
st.plotly_chart(fig)
