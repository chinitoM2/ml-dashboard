import matplotlib as plt
import plotly.express as pxp
import streamlit as st

cmap1 = plt.cm.get_cmap('jet')
def create_material_summary(df):
  material_df = df.groupby(by=['product_type', 'material'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  with st.expander('Material Summary_View Data:'):
    st.table(material_df.style.background_gradient(cmap=cmap1))

    material_bar, material_pie = st.columns((2))
    with material_bar:
      st.subheader('Material Wise Orders Bar Chart')
      figBar = pxp.bar(material_df, x='product_type', y='quantity', text=material_df['material'], template='plotly')
      st.plotly_chart(figBar, use_container_width=True, height=200)
    with material_pie:
      st.subheader('Material Wise Orders Pie Chart')
      figPie = pxp.pie(material_df, values='quantity', names='material', hole=0.02)
      st.plotly_chart(figPie, use_container_width=True, height=200)