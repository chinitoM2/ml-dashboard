import matplotlib as plt
import streamlit as st
import pandas as pd

cmap1=plt.cm.get_cmap('YlGnBu')
def calc_production_times(df):
  try:
    df['pay_date'] = pd.to_datetime(df['pay_date'])
  except:
    df['pay_date'] = pd.NaT
  
  try:
    df['shipped_date'] = pd.to_datetime(df['shipped_date'])
  except:
    df['shipped_date'] = pd.NaT

  df['production_time'] = df['shipped_date'] - df['pay_date']
  df['production_time_final'] = df['production_time'].apply(lambda x: f'{x.days +1} days' if x.days > 0 & (x.seconds//3600 >43200) else f'{x.days} days' if x.days > 0 & (x.seconds//3600 <12) else f'{x.seconds // 3600} hours' if x.seconds >= 3600 else f'{x.seconds // 60} minutes' if x.seconds > 0 else '0 days' if not pd.isnull(x) else x)

  top20_production_times = df.groupby(by=['production_time_final'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(20,'quantity')
  st.header('PRODUCTION TIMES')
  with st.expander('Top 20 Common Production Times'):
    st.table(top20_production_times.style.background_gradient(cmap=cmap1))
