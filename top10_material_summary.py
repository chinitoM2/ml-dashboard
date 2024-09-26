import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top10_material_summary(df,key):
  top10_material = df.groupby(by=['material'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Most Purchased Material'):
    st.table(top10_material.style.background_gradient(cmap=cmap1))
    csv = top10_material.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top10_most_purchased_material_totals.csv',mime='text/csv',key=key)