import streamlit as st
import matplotlib.pyplot as plt

cmap1 = plt.cm.get_cmap('RdYlGn')
def create_quantity_under6_product_summary(df):
  product_df = df.groupby(by=['product_type'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False).reset_index(drop=True)
  with st.expander('Product Totals where Quantity Exlcudes >5 Summary_View Data:'):
    st.table(product_df.style.background_gradient(cmap=cmap1))
    