import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_shipping_companies_summary(df):
  shipping_companies_df = df.groupby(by=['shipping_companies'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False)
  st.header('SHIPPING COMPANIES')
  with st.expander('Most Used Shipping Companies'):
    st.table(shipping_companies_df.style.background_gradient(cmap=cmap1))
    csv = shipping_companies_df.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='shipping_companies_totals.csv',mime='text/csv',)