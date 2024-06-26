import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top9_LxW_summary(df,key):
  top9_lxw = df.groupby(by=['LxW'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased LxW'):
    st.table(top9_lxw.style.background_gradient(cmap=cmap1))
    csv = top9_lxw.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_purchased_lxw_totals.csv',mime='text/csv',key=key)