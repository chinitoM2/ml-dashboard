import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import yaml

from bubblemap import create_bubblemap
from colorgroup_summary import create_colorgroup_summary
from data_controller import load_data
from data_filters import filter_data
from date_picker import pick_date
from framenumber_summary import create_framenumber_summary
from material_summary import create_material_summary
from mirror_measurement_summary import create_mirror_measurement_summary
from quantity_under6_product_summary import create_quantity_under6_product_summary
from states_orders_summary import create_states_order_summary
from table_summary import create_table_summary
from tri_report import create_tri_report
from yaml.loader import SafeLoader

def main():
  st.set_page_config(page_title='MirrorLot 💯💯', page_icon=':bar_chart:', layout='wide')
  with open('/Users/thomasss/Desktop/mirrorlot/ml_streamlit_plotly_dashboard/config.yaml') as file:
    config = yaml.load(file,Loader=SafeLoader)
  authenticator = stauth.Authenticate(config['credentials'],config['cookie']['name'],config['cookie']['key'],config['cookie']['expiry_days'])
  name, authentication_status, username = authenticator.login('Login', 'main')
  if authentication_status==False:
    st.error('Username and/or password is incorrect')
  if authentication_status==None:
    st.warning('Please enter your username and password')
  if authentication_status:
    st.title(':100: MirrorLot :100:')
    st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
    authenticator.logout('Logout','sidebar')
    st.sidebar.title(f'Welcome {name}')

  # UPLOAD DATA FILE
  df = load_data()

  # DATE PICKER COLUMN CONTAINERS
  col_startDate, col_endDate = st.columns((2))
  startDate, endDate = pick_date(df)
  with col_startDate:
    date1 = pd.to_datetime(st.date_input('Start Date', startDate))
  with col_endDate:
    date2 = pd.to_datetime(st.date_input('End Date', endDate))
  df = df[(df['pay_date'] >= date1) & (df['pay_date'] <= date2)].copy()

  # DATA FILTERS
  st.sidebar.header('Choose your filter: ')
  filtered_df = filter_data(df)
  qty_under6_df = filtered_df[filtered_df['quantity']<6]
  #mirror_orders = filtered_df[filtered_df['Frame_Number'].notna()]
  #table_orders = filtered_df[filtered_df['TableTop_Number'].notna()]

  # DATA REPORTS AND VISUALIZATIONS
  create_tri_report(qty_under6_df)
  st.header('OTHER REPORTS')
  create_quantity_under6_product_summary(qty_under6_df)
  create_states_order_summary(qty_under6_df)
  #create_states_order_summary(filtered_df)
  create_bubblemap(filtered_df)
  #create_material_summary(filtered_df)
  #create_colorgroup_summary(filtered_df)
  #create_framenumber_summary(mirror_orders)
  #create_mirror_measurement_summary(mirror_orders)
  #create_table_summary(table_orders)

if __name__ == '__main__':
  main()
