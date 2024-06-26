import streamlit as st

from quantity_under6_product_summary import create_quantity_under6_product_summary
from top9_frame_summary import create_top9_frame_summary
from top9_height_summary import create_top9_height_summary
from top9_width_summary import create_top9_width_summary
from top9_measurement_summary import create_top9_measurement_summary

def create_mirror_summary(df):
  st.header('MIRROR SUMMARY')
  col1, col2 = st.columns((2))
  with col1:
    create_quantity_under6_product_summary(df)
    create_top9_width_summary(df,'mirror_top9_width')
    create_top9_frame_summary(df)
  with col2:
    create_top9_measurement_summary(df,'mirror_top9_wxh')
    create_top9_height_summary(df,'mirror_top9_height')