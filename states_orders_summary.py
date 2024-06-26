import matplotlib.pyplot as plt
import plotly.express as pxp
import streamlit as st

from pie_chart import pie

cmap2 = plt.cm.get_cmap('jet')
def create_states_order_summary(df):
  state_totals = df.groupby(by=['states'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  top5_states = state_totals.nlargest(5, 'quantity')
  top12_states = state_totals.nlargest(12, 'quantity')
  with st.expander('State Totals Summary_View Data:'):
    st.table(state_totals.style.background_gradient(cmap=cmap2))
  
    states_bar1, states_pie1 = st.columns((2))
    with states_bar1:
      st.subheader('State Wise Orders')
      figBar = pxp.bar(state_totals, x='states', y='quantity', text=state_totals['quantity'], template='seaborn')
      figBar.update_traces(textposition='outside')
      st.plotly_chart(figBar, use_container_width=True, height=200)
    with states_pie1:
      st.subheader('State Wise Orders')
      figPie = pie(df, values='quantity', names='states', hole=0.02, hovertemplate='%{label} <br> Quantity Shipped: %{value} <br>')
      figPie.update_traces(text=df['states'], textposition='inside', textinfo='label+percent')
      st.plotly_chart(figPie, use_container_width=True)

  with st.expander('Top 5 States Totals_View Data:'):
    st.table(top5_states.style.background_gradient(cmap=cmap2))
  
    top5_bar1, top5_pie1 = st.columns((2))
    with top5_bar1:
      st.subheader('Top 5 State Wise Orders')
      figBar = pxp.bar(top5_states, x='states', y='quantity', text=top5_states['quantity'], template='seaborn')
      figBar.update_traces(textposition='outside')
      st.plotly_chart(figBar, use_container_width=True, height=200)
    with top5_pie1:
      st.subheader('Top 5 State Wise Orders')
      figPie = pie(top5_states, values='quantity', names='states', hole=0.02, hovertemplate='%{label} <br> Quantity Shipped: %{value} <br>')
      figPie.update_traces(text=top5_states['states'], textposition='inside', textinfo='label+percent')
      st.plotly_chart(figPie, use_container_width=True)

  with st.expander('Top 12 States Totals_View Data:'):
    st.table(top12_states.style.background_gradient(cmap=cmap2))
  
    top12_bar1, top12_pie1 = st.columns((2))
    with top12_bar1:
      st.subheader('Top 12 State Wise Orders')
      figBar = pxp.bar(top12_states, x='states', y='quantity', text=top12_states['quantity'], template='seaborn')
      figBar.update_traces(textposition='outside')
      st.plotly_chart(figBar, use_container_width=True, height=200)
    with top12_pie1:
      st.subheader('Top 12 State Wise Orders')
      figPie = pie(top12_states, values='quantity', names='states', hole=0.02, hovertemplate='%{label} <br> Quantity Shipped: %{value} <br>')
      figPie.update_traces(text=top12_states['states'], textposition='inside', textinfo='label+percent')
      st.plotly_chart(figPie, use_container_width=True)