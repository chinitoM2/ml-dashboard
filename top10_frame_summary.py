import matplotlib as plt
import streamlit as st

cmap1 = plt.cm.get_cmap('YlGnBu')
def create_top10_frame_summary(df):
  frame_totals = df.groupby(by=['frame_number'],as_index=False)['quantity'].sum().sort_values(by='quantity',ascending=False)
  top10_frames = frame_totals.nlargest(10,'quantity').reset_index(drop=True)
  with st.expander('Top 10 Frames'):
    st.table(top10_frames.style.background_gradient(cmap=cmap1))
    csv = top10_frames.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data',data=csv,file_name='ml_top10_frame_totals.csv',mime='text/csv',key='top10_frame')