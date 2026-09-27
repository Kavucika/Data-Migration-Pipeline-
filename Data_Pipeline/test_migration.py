{
  "source": "oracle",
  "target": "postgresql",
  "data_extraction": [
    "SELECT c.customer_id, c.email_address, c.full_name, o.order_id, o.order_tms, o.order_status FROM CUSTOMERS c INNER JOIN ORDERS o ON c.customer_id = o.customer_id",
    "SELECT product_id, product_name, unit_price FROM PRODUCTS",
    "SELECT product_id, product_image, image_mime_type, image_filename, image_charset, image_last_updated FROM PRODUCTS"
  ],
  "data_management": [
    "INSERT INTO public.test_customer_orders (customer_id, email_address, full_name, order_id, order_tms, order_status) VALUES {VALUES_PLACEHOLDER};",
    "INSERT INTO public.test_product_details (product_id, product_name, unit_price) VALUES {VALUES_PLACEHOLDER};",
    "INSERT INTO public.test_product_images (product_id, product_image, image_mime_type, image_filename, image_charset, image_last_updated) VALUES {VALUES_PLACEHOLDER};"
  ]
}