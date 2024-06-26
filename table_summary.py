import streamlit as st

from top5_table_with_base_measurements_summary import create_top5_table_with_base_measurements_summary
from top5_tableleg_number_summary import create_top5_tableleg_number_summary
from top5_tabletop_number_summary import create_top5_tabletop_number_summary
from top12_table_productname_summary import create_top12_table_productname_summary
def create_table_summary(df):
  table_with_base_orders = df[df['tableleg_number'].notna()]
  #tatable_top_only = df[df['tableleg_number'].isna()]
  col1, col2 = st.columns((2))
  with col1:
    create_top5_table_with_base_measurements_summary(table_with_base_orders)
    create_top5_tableleg_number_summary(table_with_base_orders)
  with col2:
    create_top5_tabletop_number_summary(df)
    create_top12_table_productname_summary(df)