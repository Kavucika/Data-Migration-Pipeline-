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



# 2.
{
  "result": {
    "schema_design": {
      "provider": "groq",
      "status": "recommended",
      "summary": "FIRST_NAME set to NOT NULL, keys preserved.",
      "issue_reason": "",
      "target_schema": {
        "tables": [
          {
            "tableName": "EMPLOYEES",
            "columns": [
              {
                "columnName": "EMPLOYEE_ID",
                "dataType": "INTEGER",
                "dataLength": -1,
                "dataPrecision": -1,
                "dataScale": -1,
                "nullable": "N",
                "dataDefault": "",
                "columnId": 1
              },
              {
                "columnName": "FIRST_NAME",
                "dataType": "VARCHAR",
                "dataLength": 50,
                "dataPrecision": -1,
                "dataScale": -1,
                "nullable": "N",
                "dataDefault": "",
                "columnId": 2
              }
            ],
            "primaryKey": {
              "constraintName": "EMPLOYEES_PK",
              "columns": [
                "EMPLOYEE_ID"
              ]
            },
            "foreignKeys": []
          }
        ]
      }
    },
    "table_management": {
      "provider": "groq",
      "source": "oracle",
      "target": "postgresql",
      "table_management": [
        "CREATE TABLE IF NOT EXISTS public.employees (employee_id INTEGER NOT NULL, first_name VARCHAR(50) NOT NULL);",
        "ALTER TABLE public.employees ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);"
      ],
      "plan": {
        "create": [
          "EMPLOYEES"
        ],
        "drop": [],
        "type_mappings": [
          {
            "table": "EMPLOYEES",
            "column": "EMPLOYEE_ID",
            "oracle": "NUMBER",
            "postgresql": "INTEGER"
          },
          {
            "table": "EMPLOYEES",
            "column": "FIRST_NAME",
            "oracle": "VARCHAR2",
            "postgresql": "VARCHAR"
          }
        ]
      },
      "summary": "Created 1 table and dropped 0 tables."
    },
    "files": [
      {
        "path": "migration/postgres/schema/target_schema.json",
        "kind": "schema"
      },
      {
        "path": "migration/postgres/ddl/001_create_table_employees.sql",
        "kind": "table_management",
        "index": 0,
        "statement": "CREATE TABLE IF NOT EXISTS public.employees (employee_id INTEGER NOT NULL, first_name VARCHAR(50) NOT NULL);"
      },
      {
        "path": "migration/postgres/ddl/002_alter_table_add_constraint_employees_pkey.sql",
        "kind": "table_management",
        "index": 1,
        "statement": "ALTER TABLE public.employees ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);"
      },
      {
        "path": "migration/manifest.json",
        "kind": "manifest"
      }
    ]
  },
  "layout": {
    "bundle_root": "migration",
    "source_schema": "migration/oracle/schema/source_schema.json",
    "target_schema": "migration/postgres/schema/target_schema.json",
    "ddl": "migration/postgres/ddl",
    "manifest": "migration/manifest.json"
  }
}