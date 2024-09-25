import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('jet')
def create_top10_height_summary(df,key):
  df['height'] = df['height'].astype(str)
  height_df = df.groupby(by=['height'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False)
  top10_height = height_df.nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Most Purchased Height'):
    st.table(top10_height.style.background_gradient(cmap=cmap1))
    csv = top10_height.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top10_most_purchased_height_totals.csv',mime='text/csv',key=key)
