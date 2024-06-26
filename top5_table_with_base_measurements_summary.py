import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap2 = plt.cm.get_cmap('Blues')
def create_top5_table_with_base_measurements_summary(df):
  measurement_totals = df.groupby(by=['measurement'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  top5_measurement_totals = measurement_totals.nlargest(5, 'quantity')
  with st.expander('Top 5 Table with Base Measurements Summary_View Data:'):
    st.table(top5_measurement_totals.style.background_gradient(cmap=cmap2))
    csv = top5_measurement_totals.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name='top5_table_with_base_measurement_totals.csv', mime='text/csv', help='Click here to download the top 5 table with base measurement data as a csv file')
    