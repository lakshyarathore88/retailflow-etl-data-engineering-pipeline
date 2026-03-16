import pandas as pd

# CSV load
df = pd.read_csv("data/raw/olist_orders_dataset.csv")

null_count = df['order_id'].duplicated().sum()

print(null_count)