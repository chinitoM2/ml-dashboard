import matplotlib as plt
import streamlit as st

cmap1 = plt.cm.get_cmap('jet')
def create_framenumber_summary(df):
  frame_totals = df.groupby(by=['frame_number'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  with st.expander('Frame Number Summary_View Data:'):
    st.table(frame_totals.style.background_gradient(cmap=cmap1))
    csv = frame_totals.to_csv(index=False).encode('utf-8')
    st.download_button('Download Data', data=csv, file_name='ml_frame_totals.csv', mime='text/csv', help='Click here to download the frame number data as a csv')
