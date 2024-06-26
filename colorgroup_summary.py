import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap1 = plt.cm.get_cmap('jet')
def create_colorgroup_summary(df):
  colorgroup_df = df.groupby(by=['colorgroup', 'product_type'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  with st.expander('Colorgroup Summary_View Data:'):
    st.table(colorgroup_df.style.background_gradient(cmap=cmap1))

    colorgroup_bar, colorgroup_pie = st.columns((2))
    with colorgroup_bar:
      st.subheader('Colorgroup Wise Orders Bar Chart')
      figBar = pxp.bar(colorgroup_df, x='product_type', y='quantity', text=colorgroup_df['colorgroup'], template='plotly')
      st.plotly_chart(figBar, use_container_width=True, height=200)
    with colorgroup_pie:
      st.subheader('Colorgroup Wise Orders Pie Chart')
      figPie = pxp.pie(colorgroup_df, values='quantity', names='colorgroup', hole=0.02)
      st.plotly_chart(figPie, use_container_width=True, height=200)