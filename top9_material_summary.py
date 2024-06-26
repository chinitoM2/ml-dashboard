import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('YlGnBu')
def create_top9_material_summary(df,key):
  top9_material = df.groupby(by=['material'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False).nlargest(9,'quantity')
  with st.expander('Top 9 Most Purchased Material'):
    st.table(top9_material.style.background_gradient(cmap=cmap1))
    csv = top9_material.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='top9_most_purchased_material_totals.csv',mime='text/csv',key=key)