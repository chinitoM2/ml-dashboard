import streamlit as st

from top9_height_summary import create_top9_height_summary
from top9_LxW_summary import create_top9_LxW_summary
from top9_length_summary import create_top9_length_summary
from top9_material_summary import create_top9_material_summary
from top9_tableleg_summary import create_top9_tableleg_summary
from top9_width_summary import create_top9_width_summary

def create_table_w_base_summary(df):
  # most purchased LxW, length, width, height, lumbar material, table leg
  st.header('TABLE WITH BASE SUMMARY')
  table_w_base_col1, table_w_base_col2 = st.columns((2))
  with table_w_base_col1:
    create_top9_LxW_summary(df,'table_w_base_top9_lxw')
    create_top9_width_summary(df,'table_w_base_top9_width')
    create_top9_material_summary(df,'table_w_base_top9_material')
  with table_w_base_col2:
    create_top9_length_summary(df,'table_w_base_top9_length')
    create_top9_height_summary(df,'table_w_base_top9_height')
    create_top9_tableleg_summary(df)

def create_tabletop_summary(df):
  # most purchased LxW, length, width, lumbar material
  st.header('TABLE TOP SUMMARY')
  tabletop_col1, tabletop_col2 = st.columns((2))
  with tabletop_col1:
    create_top9_LxW_summary(df,'tabletop_top9_lxw')
    create_top9_width_summary(df,'tabletop_top9_width')
  with tabletop_col2:
    create_top9_length_summary(df,'tabletop_top9_length')
    create_top9_material_summary(df,'tabletop_top9_material')
    
