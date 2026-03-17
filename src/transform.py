import pandas as pd
import os

# -----------------------------
# LOAD DATA
# -----------------------------
def load_data():
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
    products = pd.read_csv("data/raw/olist_products_dataset.csv")
    sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")
    order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

    return orders, customers, products, sellers, order_items


# -----------------------------
# DIMENSION TABLES
# -----------------------------
def create_dim_customers(customers):
    return customers[['customer_id', 'customer_city', 'customer_state']].drop_duplicates()


def create_dim_products(products):
    return products[['product_id', 'product_category_name']].drop_duplicates()


def create_dim_sellers(sellers):
    return sellers[['seller_id', 'seller_city', 'seller_state']].drop_duplicates()


def create_dim_date(orders):
    df = pd.DataFrame()
    df['date'] = pd.to_datetime(orders['order_purchase_timestamp'])

    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    return df.drop_duplicates()


# -----------------------------
# FACT TABLE
# -----------------------------
def create_fact_orders(orders, order_items):

    # aggregate order_items
    order_items_agg = order_items.groupby('order_id').agg({
        'price': 'sum',
        'freight_value': 'sum'
    }).reset_index()

    # join with orders
    fact = orders.merge(order_items_agg, on='order_id', how='left')

    return fact[[
        'order_id',
        'customer_id',
        'order_purchase_timestamp',
        'price',
        'freight_value'
    ]]


# -----------------------------
# SAVE TABLES
# -----------------------------
def save_tables(dim_customers, dim_products, dim_sellers, dim_date, fact_orders):

    os.makedirs("data/warehouse", exist_ok=True)

    dim_customers.to_csv("data/warehouse/dim_customers.csv", index=False)
    dim_products.to_csv("data/warehouse/dim_products.csv", index=False)
    dim_sellers.to_csv("data/warehouse/dim_sellers.csv", index=False)
    dim_date.to_csv("data/warehouse/dim_date.csv", index=False)
    fact_orders.to_csv("data/warehouse/fact_orders.csv", index=False)


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def run_pipeline():

    print("🚀 Pipeline started...")

    orders, customers, products, sellers, order_items = load_data()

    print("✅ Data Loaded")

    dim_customers = create_dim_customers(customers)
    dim_products = create_dim_products(products)
    dim_sellers = create_dim_sellers(sellers)
    dim_date = create_dim_date(orders)

    print("✅ Dimension tables created")

    fact_orders = create_fact_orders(orders, order_items)

    print("✅ Fact table created")

    save_tables(dim_customers, dim_products, dim_sellers, dim_date, fact_orders)

    print("🎯 Star Schema created in data/warehouse/")


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    run_pipeline()