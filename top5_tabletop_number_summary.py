import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap1 = plt.cm.get_cmap('jet')
def create_top5_tabletop_number_summary(df):
  tabletop_number_totals = df.groupby(by=['tabletop_number'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  top5_tabletop_number = tabletop_number_totals.nlargest(5,'quantity')
  with st.expander('Top 5 TableTop Number Summary_View Data:'):
    st.table(top5_tabletop_number.style.background_gradient(cmap=cmap1))
    csv = top5_tabletop_number.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name='top5_tabletop_number_totals.csv', mime='text/csv', help='Click here to download the top 5 tabletop number data as a csv file')
    figBar = pxp.bar(top5_tabletop_number, x='tabletop_number', y='quantity', text=top5_tabletop_number['tabletop_number'], template='plotly')
    st.plotly_chart(figBar, use_container_width=True, height=200)
