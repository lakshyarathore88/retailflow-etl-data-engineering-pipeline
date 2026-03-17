# import pandas as pd



# # CSV load
# df = pd.read_csv("data/processed/olist_orders_datase.csv", parse_dates=["order_estimated_delivery_date"])



# # convert estimated date
# df["order_estimated_delivery_date"] = pd.to_datetime(
#     df["order_estimated_delivery_date"], errors="coerce", utc=True
# )

# # convert delivered date (agar pehle nahi kiya)
# df["order_delivered_customer_date"] = pd.to_datetime(
#     df["order_delivered_customer_date"], errors="coerce", utc=True
# )

# # calculate delay
# df["delivery_delay_days"] = (
#     df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
# ).dt.days


# df.to_csv("data/processed/olist_orders_datase.csv", index=False)


import pandas as pd

df = pd.read_csv("data/raw/olist_order_items_dataset.csv", dtype=str)

print(df["freight_value"].dtype)



