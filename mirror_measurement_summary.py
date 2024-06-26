import matplotlib as plt
import streamlit as st

cmap1=plt.cm.get_cmap('jet')
def create_mirror_measurement_summary(df):
  measurement_totals = df.groupby(by=['measurement'], as_index=False)['quantity'].sum().sort_values(by='quantity', ascending=False)
  with st.expander('Mirror Measurement Summary_View Data:'):
    st.table(measurement_totals.style.background_gradient(cmap=cmap1))
    csv = measurement_totals.to_csv(index=False).encode('utf-8')
    st.download_button('Download Button', data=csv, file_name='ml_mirror_measurement_totals.csv', mime='text/csv', help='Click here to download the mirror measurement data as a csv file')