## Table: olist_orders_dataset.csv
Rows: 2000 | Columns: 8

### order_id
- Type: String (32-character MD5 hash)
- Nullable: NO (in theory) — but check for duplicates (i have checked 0 null)
- Sample value: e481f51cbdc54678b7cc49136f2d6af7
- Issue found: 80 duplicates
- Transform needed: Deduplicate keeping highest lifecycle status [Done]

### customer_id
- Type: String (32-character MD5 hash)
- Nullable: YES — 0 null
- Sample value: 9ef432eb6251297304e76186b10a928d
- Note: This is NOT the same as customer_unique_id (see customers table)
- Issue found: 1136 duplicated
- Transform needed: [No deduplication required - customer_id represents an order-level identifier and duplicates are expected when an order contains multiple rows (e.g., multiple items).]

### order_status
- Type: Categorical string (ENUM)
- Nullable: 0
- Valid values: delivered, shipped, cancelled, processing, invoiced, unavailable, approved
- Issue found: [[No mixed casing observerd] — is there mixed casing? e.g. 'DELIVERED'?]
- Transform needed: LOWER() + strip whitespace + validate against enum list [DONE]

### order_purchase_timestamp
- Type: Timestamp
- Nullable: YES — [20 null, 1%]
- Formats observed: [ISO]
  - Example 1 (ISO):05/23/2018 08:32
  - Example 2 (US format): Not observed
  - Example 3 (month name): Not observed
  - Example 4 (Unix epoch): Not observed
- Issue found: Mixed formats + nulls + [0 count of delivery-before-purchase]
- Transform needed: Detect format → parse → convert to UTC [Done]

### order_approved_at
- Type: Timestamp
- Nullable: YES — [153]
- Note: NULL for cancelled orders is EXPECTED and VALID — not a data error
- Transform needed: Parse to UTC, preserve nulls [Done]

### order_delivered_carrier_date
- Type: Timestamp
- Nullable: YES — [311]
- Note: NULL for orders that haven't been picked up by carrier yet — expected
- Transform needed: Parse to UTC, preserve nulls [Done]

### order_delivered_customer_date
- Type: Timestamp
- Nullable: YES — [613]
- CRITICAL ISSUE: [32 — how many rows have this BEFORE order_purchase_timestamp?]
- Transform needed: Parse to UTC; quarantine rows where delivered < purchased [Done]

### order_estimated_delivery_date
- Type: Date (no time component)
- Nullable: 0
- Use: Key input for computing delivery_delay_days KPI
- Transform needed: Parse date; compute delivery_delay_days = delivered - estimated [Done]

