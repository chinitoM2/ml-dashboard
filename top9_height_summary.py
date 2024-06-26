import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('jet')
def create_top9_height_summary(df,key):
  height_df = df.groupby(by=['height'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False)
  top9_height = height_df.nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased Height'):
    st.table(top9_height.style.background_gradient(cmap=cmap1))
    csv = top9_height.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_purchased_height_totals.csv',mime='text/csv',key=key)
