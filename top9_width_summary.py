import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top9_width_summary(df,key):
  top9_width = df.groupby(by=['width'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased Width'):
    st.table(top9_width.style.background_gradient(cmap=cmap1))
    csv = top9_width.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_purhcased_width_totals',mime='text/csv',key=key)