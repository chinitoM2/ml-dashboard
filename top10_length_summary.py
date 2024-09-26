import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top10_length_summary(df,key):
  #product_type = df.loc[2].at['Product_Type']
  df['length'] = df['length'].astype(str)
  top10_length = df.groupby(by=['length'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Most Purchased Length'):
    st.table(top10_length.style.background_gradient(cmap=cmap1))
    csv = top10_length.to_csv(index=False).encode('utf-8')
    st.download_button('Downlaod Data',data=csv,file_name='top10_most_purchased_length_totals',mime='text/csv',key=key)