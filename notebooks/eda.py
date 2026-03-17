# import pandas as pd

# CSV load
# df = pd.read_csv("data/processed/olist_orders_datase.csv", parse_dates=["order_estimated_delivery_date"])

# df = pd.read_csv("data/raw/olist_order_items_dataset.csv", parse_dates=["shipping_limit_date"])

# df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"],errors="coerce",utc=True)


#check datatype
# print(df["shipping_limit_date"].dtype)

# invalid_mask = (
#     df["order_delivered_customer_date"] < df["order_purchase_timestamp"]
# )


# Quarantine dataset
# df_quarantine = df[invalid_mask]

# Clean dataset
# df_clean = df[~invalid_mask]

# print("Invalid rows (delivered before purchased):", df_quarantine)
# print("Clean rows:", len(df_clean))

# Parse estimated delivery date
# df["order_estimated_delivery_date"] = pd.to_datetime(
#     df["order_estimated_delivery_date"], errors="coerce"
# )

# Calculate delivery delay in days
# df["delivery_delay_days"] = (
#     df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
# ).dt.days



# df.to_csv("data/raw/olist_order_items_dataset.csv", index=False)




# df_quarantine.to_csv("data/quarantine/orders_invalid_delivery.csv", index=False)





# olist_order_items_dataset — Transform

# import pandas as pd

# df = pd.read_csv("data/raw/olist_order_items_dataset.csv", dtype=str)

# # numeric convert
# df["price"] = pd.to_numeric(df["price"], errors="coerce")
# df["freight_value"] = pd.to_numeric(df["freight_value"], errors="coerce")

# # aggregation
# agg = df.groupby("order_id").agg({
#     "price": "sum",
#     "freight_value": "sum",
#     "order_item_id": "count"
# }).rename(columns={
#     "price": "total_price",
#     "freight_value": "total_freight",
#     "order_item_id": "item_count"
# }).reset_index()

# # SAVE FILE 🔥
# agg.to_csv("data//order_items_agg.csv", index=False)

# print("Saved successfully ✅")






# olist_order_payments_dataset - Transform 

# import pandas as pd

# df = pd.read_csv("data/raw/olist_order_payments_dataset.csv", dtype=str)

# # numeric
# df["payment_value"] = pd.to_numeric(df["payment_value"], errors="coerce")

# # aggregation
# agg = df.groupby("order_id").agg({
#     "payment_value": "sum",
#     "payment_type": lambda x: ",".join(x.unique())
# })

# print(agg.head())


# agg.to_csv("data/processed/order_payment_agg.csv", index=False)


# SELLER Transform

# import pandas as pd


# df = pd.read_csv('data/raw/olist_sellers_dataset.csv', dtype=str)

# df['seller_city'] = df['seller_city'].replace(
#     ["N/A", "n/a", "unknown", "-"], pd.NA)


# df.to_csv('data/raw/olist_sellers_dataset.csv', index=False)


# olist_products_dataset - Transform


# import pandas as pd

# df = pd.read_csv("data/raw/olist_products_dataset.csv", dtype=str)

# # FIX TYPO (must do)
# df = df.rename(columns={
#     "product_name_lenght": "product_name_length",
#     "product_description_lenght": "product_description_length"
# })

# # numeric
# df["product_weight_g"] = pd.to_numeric(df["product_weight_g"], errors="coerce")


# # category null fix
# df["product_category_name"] = df["product_category_name"].fillna("unknown")


# print(df.head())

# df.to_csv("data/raw/olist_products_dataset.csv", index=False)


import pandas as pd

df = pd.read_csv("data/raw/olist_geolocation_dataset.csv")


print(df["geolocation_lng"].dtype)


