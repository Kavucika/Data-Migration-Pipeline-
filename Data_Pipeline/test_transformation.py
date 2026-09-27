{
  "source": "oracle",
  "target": "postgresql",
  "table_management": [
    "CREATE TABLE public.test_customer_orders (customer_id INTEGER NOT NULL, email_address VARCHAR(255) NOT NULL, full_name VARCHAR(255) NOT NULL, order_id INTEGER NOT NULL, order_tms TIMESTAMP NOT NULL, order_status VARCHAR(40) NOT NULL);",
    "ALTER TABLE public.test_customer_orders ADD CONSTRAINT test_customer_orders_pk PRIMARY KEY (order_id);",
    "CREATE TABLE public.test_product_details (product_id INTEGER NOT NULL, product_name VARCHAR(255) NOT NULL, unit_price NUMERIC(10,2));",
    "ALTER TABLE public.test_product_details ADD CONSTRAINT test_product_details_pk PRIMARY KEY (product_id);",
    "CREATE TABLE public.test_product_images (product_id INTEGER NOT NULL, product_image BYTEA, image_mime_type VARCHAR(255), image_filename VARCHAR(255), image_charset VARCHAR(255), image_last_updated TIMESTAMP);",
    "ALTER TABLE public.test_product_images ADD CONSTRAINT test_product_images_pk PRIMARY KEY (product_id);"
  ]
}
