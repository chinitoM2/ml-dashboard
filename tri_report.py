from customer_decision_times import calc_customer_decision_times
from customer_summary import create_customer_visit_count_summary, create_time_of_day_customer_bought_summary, create_part_of_day_customer_bought_summary, create_time_of_day_customer_first_visit_summary, create_part_of_customer_first_visit_summary, create_day_of_week_customer_bought_summary, create_day_of_week_first_visit_summary, create_month_customer_bought_summary, create_month_first_visit_summary, create_quarter_customer_bought_summary, create_quarter_first_visit_summary
from geospational_summary import create_top20_zipcode_summary, create_top20_counties_summary
from mirror_summary import create_mirror_summary
from production_times import calc_production_times
from shipping_companies import create_shipping_companies_summary
from tri_table_summary import create_tabletop_summary
from tri_table_summary import create_table_w_base_summary

def create_tri_report(df):
  mirror_orders = df[df['frame_number'].notna()]
  table_orders = df[df['tabletop_number'].notna()]
  table_with_base_orders = table_orders[table_orders['tableleg_number'].notna()]
  shipping_companies = df[df['shipping_companies'] != 'other or tracking number only']
  valid_lead_date_first_visit = df[df['lead_date_first_visit'].notna()]
  # MIRROR SUMMARY (most purchased WxH, width, height, frame)
  create_mirror_summary(mirror_orders)
  # TABLE WITH BASE SUMMARY (most purchased LxW, length, width, height, lumbar material, table leg)
  create_table_w_base_summary(table_with_base_orders)
  # TABLE TOP SUMMARY (most purchased LxW, length, width, lumbar material)
  create_tabletop_summary(table_orders)
  # TRACKING NUMBER (list shipping companies from most 2 least, excluding qty>5)
  create_shipping_companies_summary(shipping_companies)
  # MOST COMMON PRODUCTION TIMES
  calc_production_times(df)
  # MOST COMMON CUSTOMER DECISION TIME BY DAYS
  calc_customer_decision_times(df)
  # TOP 20 ZIP CODES, CITIES, STATES, COUNTIES
  create_top20_zipcode_summary(df)
  create_top20_counties_summary(df)
  # TOP 10 DOMAINS
  # COMMON COUNT OF CUSTOMER VISITS B4 BUYING
  create_customer_visit_count_summary(df)
  # COMMON TIME OF DAY CUSTOMERS BUY
  create_time_of_day_customer_bought_summary(df)
  create_part_of_day_customer_bought_summary(df)
  create_day_of_week_customer_bought_summary(df)
  create_month_customer_bought_summary(df)
  create_quarter_customer_bought_summary(df)
  # COMMON TIME OF DAY CUSTOMER VISIT SITE 4 FIRST TIME
  create_time_of_day_customer_first_visit_summary(df)
  create_part_of_customer_first_visit_summary(valid_lead_date_first_visit)
  create_day_of_week_first_visit_summary(valid_lead_date_first_visit)
  create_month_first_visit_summary(valid_lead_date_first_visit)
  create_quarter_first_visit_summary(valid_lead_date_first_visit)