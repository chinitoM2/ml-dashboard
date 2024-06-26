import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

cmap2 = plt.cm.get_cmap('jet')
def create_bubblemap(df):
  #po_cities_totals = df.groupby('post office cities', as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  df['quantity'] = df['quantity'].astype(int)
  df['latitudes'] = df['latitudes'].astype(float)
  df['longitudes'] = df['longitudes'].astype(float)
  po_cities_totals_geocoordinates = df.groupby('post_office_cities', as_index=False).agg({'longitudes':'first','latitudes':'first','quantity':'sum'}).sort_values(by='quantity', ascending=False)
  #po_cities_totals_geocoordinates = df.groupby('post office cities', as_index=False).agg({'longitudes':'first','latitudes':'first','quantity':'sum'})
  #with st.expander('Post Office Cities Totals Summary_View Data:'):
    #st.table(po_cities_totals.style.background_gradient(cmap=cmap2))
  
  
  po_cities_totals_geocoordinates['text'] = po_cities_totals_geocoordinates['post_office_cities'] + '<br>Quantity ' + po_cities_totals_geocoordinates['quantity'].astype(str)
  with st.expander('Post Office Cities Totals Summary with Coordinates_View Data:'):
    st.table(po_cities_totals_geocoordinates.style.background_gradient(cmap=cmap2))

  limits = [(0,5),(6,20),(21,42),(43,91),(92,112),(113,420),(421,1120),(1121,6000)]
  colors = ['royalblue','crimson','lightseagreen','orange','lightgrey','yellow','purple','brown']
  scale = 2

  fig = go.Figure()
  for i in range(len(limits)):
    lim = limits[i]
    po_cities_totals_sub = po_cities_totals_geocoordinates[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
      locationmode = 'USA-states',
      lon = po_cities_totals_sub['longitudes'],
      lat = po_cities_totals_sub['latitudes'],
      text = po_cities_totals_sub['text'],
      marker = dict(
        size = po_cities_totals_sub['quantity']*scale,
        color = colors[i],
        line_color = 'rgb(40,40,40)',
        line_width = 0.5,
        sizemode = 'area'
      ),
      name = '{0} - {1}'.format(lim[0],lim[1])
    ))
  fig.update_layout(
    title_text = 'Total Orders by Post Office City<br>(Click legend to toggle traces)',
    showlegend = True,
    geo = dict(
      scope = 'usa',
      landcolor = 'rgb(217,217,217)',
    )
  )
  with st.expander('Post Office Cities Totals Bubblemap_View Map:'):
    st.plotly_chart(fig, use_container_width=True)