import pandas as pd

def pick_date(df):
  df['pay_date'] = pd.to_datetime(df['pay_date'])
  startDate = pd.to_datetime(df['pay_date']).min()
  endDate = pd.to_datetime(df['pay_date']).max()

  return startDate, endDate