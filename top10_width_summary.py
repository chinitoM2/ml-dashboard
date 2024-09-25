import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top10_width_summary(df,key):
  df['width'] = df['width'].astype(str)
  top10_width = df.groupby(by=['width'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Most Purchased Width'):
    st.table(top10_width.style.background_gradient(cmap=cmap1))
    csv = top10_width.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top10_most_purhcased_width_totals',mime='text/csv',key=key)