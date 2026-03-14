Tables				                                Length	 Row    Encoding	BOM? 	Column	Notes
                    
olist_customers_dataset.csv           				87158	 1001	ascii	    No	    5	
olist_geolocation_dataset.csv         				115987	 2075	ascii	    No	    5	
olist_orders_dataset.csv              				312474	 2075	ascii	    No	    8	
olist_order_items_dataset.csv         				385819	 2918	ascii	    No	    7	
olist_order_payments_dataset.csv      				132076	 2414	ascii	    No	    5	
olist_order_reviews_dataset.csv       				223284	 1690	ascii	    No	    7	
olist_products_dataset.csv            				37341	 501 	ascii	    No	    9	
olist_sellers_dataset.csv             				10416	 201 	ascii	    No	    4	
product_category_name_translation.csv 				588	     21	    ascii	    No	    2	

<!-- Table: olist_customers_dataset.csv -->
Number of Columns: 5
Column Names:
- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

<!-- Table: olist_geolocation_dataset.csv -->
Number of Columns: 5
Column Names:
- geolocation_zip_code_prefix
- geolocation_lat
- geolocation_lng
- geolocation_city
- geolocation_state

<!-- Table: olist_orders_dataset.csv -->
Number of Columns: 8
Column Names:
- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_approved_at
- order_delivered_carrier_date
- order_delivered_customer_date
- order_estimated_delivery_date

<!-- Table: olist_order_items_dataset.csv -->
Number of Columns: 7
Column Names:
- order_id
- order_item_id
- product_id
- seller_id
- shipping_limit_date
- price
- freight_value

<!-- Table: olist_order_payments_dataset.csv -->
Number of Columns: 5
Column Names:
- order_id
- payment_sequential
- payment_type
- payment_installments
- payment_value

<!-- Table: olist_order_reviews_dataset.csv -->
Number of Columns: 7
Column Names:
- review_id
- order_id
- review_score
- review_comment_title
- review_comment_message
- review_creation_date
- review_answer_timestamp

<!-- Table: olist_products_dataset.csv -->
Number of Columns: 9
Column Names:
- product_id
- product_category_name
- product_name_lenght
- product_description_lenght
- product_photos_qty
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

<!-- Table: olist_sellers_dataset.csv -->
Number of Columns: 4
Column Names:
- seller_id
- seller_zip_code_prefix
- seller_city
- seller_state

<!-- Table: product_category_name_translation.csv -->
Number of Columns: 2
Column Names:
- product_category_name
- product_category_name_english

