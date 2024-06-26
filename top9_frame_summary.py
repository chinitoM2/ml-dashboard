import matplotlib as plt
import streamlit as st

cmap1 = plt.cm.get_cmap('YlGnBu')
def create_top9_frame_summary(df):
  frame_totals = df.groupby(by=['frame_number'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False)
  top9_frames = frame_totals.nlargest(9,'quantity')
  with st.expander('Top 9 Frames'):
    st.table(top9_frames.style.background_gradient(cmap=cmap1))
    csv = top9_frames.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='ml_top9_frame_totals.csv',mime='text/csv',key='top9_frame')