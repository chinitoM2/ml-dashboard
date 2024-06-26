import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top9_tableleg_summary(df):
  top9_tableleg = df.groupby(by=['tableleg_number'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased Table Leg'):
    st.table(top9_tableleg.style.background_gradient(cmap=cmap1))
    csv = top9_tableleg.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_murchased_tableleg_totals.csv',mime='text/csv')