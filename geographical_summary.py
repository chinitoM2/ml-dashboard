import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')

def create_top20_zipcode_summary(df):
  top20_zipcodes = df.groupby(by=['address_zip','post_office_cities'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(20,'quantity').reset_index(drop=True)
  top20_zipcodes['address_zip'] = top20_zipcodes['address_zip'].apply(lambda x: round(x)).astype(str)
  st.header('ZIPCODES, STATES, COUNTIES & CITIES')
  with st.expander('Top 20 Zip Codes'):
    st.table(top20_zipcodes.style.background_gradient(cmap=cmap1))

def create_top20_counties_summary(df):
  top20_counties = df.groupby(by=['counties','states'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(20,'quantity').reset_index(drop=True)
  with st.expander('Top 20 Counties'):
    st.table(top20_counties.style.background_gradient(cmap=cmap1))