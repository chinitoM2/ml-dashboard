import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap2 = plt.cm.get_cmap('Blues')
def create_top5_tableleg_number_summary(df):
  tableleg_number_totals = df.groupby(by=['tableleg_number'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  top5_tableleg_number = tableleg_number_totals.nlargest(5,'quantity')
  with st.expander('Top 5 TableLeg Number Summary_View Data:'):
    st.table(top5_tableleg_number.style.background_gradient(cmap=cmap2))
    csv = top5_tableleg_number.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name='top5_tableleg_number_totals.csv', mime='text/csv', help='Click here to download the top 5 tableleg number data as a csv file')
    figPie = pxp.pie(top5_tableleg_number, values='quantity', names='tableleg_number', hole=0.02)
    st.plotly_chart(figPie, use_container_width=True, height=200)
    