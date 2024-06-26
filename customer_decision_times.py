import matplotlib as plt
import streamlit as st
import pandas as pd

cmap1=plt.cm.get_cmap('YlGnBu')
def calc_customer_decision_times(df):
  try:
    df['pay_date'] = pd.to_datetime(df['pay_date'],errors='coerce')
  except:
    #df['pay_date'] = pd.NaT
    pass

  try:
    df['lead_date_first_visit'] = pd.to_datetime(df['lead_date_first_visit'],errors='coerce')
  except:
    pass
    #df['lead_date_first_visit'] = pd.NaT

  df['pay_date'] = df['pay_date'].astype('datetime64[ns]')
  df['lead_date_first_visit'].astype('datetime64[ns]')
  df.loc[:,'customer_decision_time'] = df['pay_date'] - df['lead_date_first_visit']
  df.loc[:,'customer_decision_time_final'] = df['customer_decision_time'].apply(lambda x: f'{x.days} days' if x.days > 0 else f'{x.seconds // 3600} hours' if x.seconds >= 3600 else f'{x.seconds // 60} minutes' if x.seconds > 0 else '0 days' if not pd.isnull(x) else x)

  top20_customer_decision_times = df.groupby(by=['customer_decision_time_final'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(20,'quantity')
  st.header('CUSTOMER DECISION TIMES')
  with st.expander('Top 20 Common Customer Decision Times'):
    st.table(top20_customer_decision_times.style.background_gradient(cmap=cmap1))
