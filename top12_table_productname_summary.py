import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap1 = plt.cm.get_cmap('jet')
def create_top12_table_productname_summary(df):
  table_name_totals = df.groupby(by=['product_name'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  top12_table_names = table_name_totals.nlargest(12,'quantity')
  with st.expander('Top 12 Table Product Names Summary_View Data:'):
    st.table(top12_table_names.style.background_gradient(cmap=cmap1))
    csv = top12_table_names.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name='top12_table_productnames_totals.csv', mime='text/csv', help='Click here to download the top 12 table productname data as a csv file')
    figPie = pxp.pie(top12_table_names, values='quantity', names='product_name', hole=0.02)
    st.plotly_chart(figPie, use_container_width=True, height=200)