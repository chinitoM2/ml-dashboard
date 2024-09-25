import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top10_tableleg_summary(df):
  top10_tableleg = df.groupby(by=['tableleg_number'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Most Purchased Table Leg'):
    st.table(top10_tableleg.style.background_gradient(cmap=cmap1))
    csv = top10_tableleg.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top10_most_murchased_tableleg_totals.csv',mime='text/csv')