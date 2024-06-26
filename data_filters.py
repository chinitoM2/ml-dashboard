import streamlit as st

def filter_data(df):
  picked_product_type = st.sidebar.multiselect('Pick the Product Type', df['product_type'].unique())
  if not picked_product_type:
    df2 = df.copy()
  else:
    df2 = df[df['product_type'].isin(picked_product_type)]
  
  sorted_states = df2['states'].sort_values(na_position='first').unique()
  state = st.sidebar.multiselect('Select State', sorted_states)
  if not state:
    df3 = df2.copy()
  else:
    df3 = df2[df2['states'].isin(state)]
  sorted_po_cities = df3['post_office_cities'].sort_values(na_position='first').unique()
  po_city = st.sidebar.multiselect('Pick the Post Office City', sorted_po_cities)

  if not picked_product_type and not state and not po_city:
    filtered_df = df
  elif not state and not po_city:
    filtered_df = df[df['product_type'].isin(picked_product_type)]
  elif not picked_product_type and not po_city:
    filtered_df = df[df['states'].isin(state)]
  elif state and po_city:
    filtered_df = df3[df['states'].isin(state) & df3['post_office_cities'].isin(po_city)]
  elif picked_product_type and state:
    filtered_df = df3[df['product_type'].isin(picked_product_type) & df3['states'].isin(state)]
  elif picked_product_type and po_city:
    filtered_df = df3[df['product_type'].isin(picked_product_type) & df3['post_office_cities'].isin(po_city)]
  elif po_city:
    filtered_df = df3[df3['post_office_cities'].isin(po_city)]
  else:
    filtered_df = df3[df3['product_type'].isin(picked_product_type) & df3['states'].isin(state) & df3['post_office_cities'].isin(po_city)]

  return filtered_df