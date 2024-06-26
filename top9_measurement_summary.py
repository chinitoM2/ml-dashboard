import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('jet')
def create_top9_measurement_summary(df,key):
  top9_wxh = df.groupby(by=['measurement'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased Measurement'):
    st.table(top9_wxh.style.background_gradient(cmap=cmap1))
    csv = top9_wxh.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_purchased_measurement_totals.csv',mime='text/csv',key=key)