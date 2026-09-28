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



# 2. 
{
    "provider": "groq",
    "result": {
        "source": "oracle",
        "target": "postgresql",
        "data_extraction": [
            "SELECT customer_id, full_name FROM EMPLOYEE;"
        ],
        "data_management": [
            "INSERT INTO public.employees (employee_id, first_name) VALUES {VALUES_PLACEHOLDER};"
        ],
        "files": [
            {
                "path": "migration/oracle/data/001_select_employee.sql",
                "group": "data_extraction",
                "index": 0,
                "statement": "SELECT DEPARTMENT_ID, DEPARTMENT_NAME FROM EMPLOYEE;"
            },
            {
                "path": "migration/oracle/data/002_select_employee.sql",
                "group": "data_extraction",
                "index": 1,
                "statement": "SELECT EMPLOYEE_ID, EMPLOYEE_NAME, DEPARTMENT_ID FROM EMPLOYEE;"
            },
            {
                "path": "migration/postgres/dml/003_insert_departments.sql",
                "group": "data_management",
                "index": 0,
                "statement": "INSERT INTO public.departments (department_id, department_name) VALUES {VALUES_PLACEHOLDER};"
            },
            {
                "path": "migration/postgres/dml/004_insert_employees.sql",
                "group": "data_management",
                "index": 1,
                "statement": "INSERT INTO public.employees (employee_id, employee_name, department_id) VALUES {VALUES_PLACEHOLDER};"
            }
        ],
        "placeholder": "{VALUES_PLACEHOLDER}",
        "summary": "Generated 2 Oracle to PostgreSQL table migration pairs."
    },
    "layout": {
        "extraction": "migration/oracle/data",
        "management": "migration/postgres/dml",
        "manifest": "migration/manifest.json"
    }
}



# final
{
  "provider": "gemini",
  "result": {
    "source": "oracle",
    "target": "postgresql",
    "data_extraction": [
      "SELECT DISTINCT E.DEPARTMENT_ID, D.DEPARTMENT_NAME FROM HR.EMPLOYEES E JOIN HR.DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID WHERE E.DEPARTMENT_ID IS NOT NULL AND D.DEPARTMENT_NAME IS NOT NULL;",
      "SELECT EMPLOYEE_ID, FIRST_NAME || ' ' || LAST_NAME AS EMPLOYEE_NAME, DEPARTMENT_ID FROM HR.EMPLOYEES;"
    ],
    "data_management": [
      "INSERT INTO public.departments (department_id, department_name) VALUES {VALUES_PLACEHOLDER};",
      "INSERT INTO public.employees (employee_id, employee_name, department_id) VALUES {VALUES_PLACEHOLDER};"
    ],
    "files": [
      {
        "path": "migration/oracle/data/001_select_employee.sql",
        "group": "data_extraction",
        "index": 0,
        "statement": "SELECT DISTINCT E.DEPARTMENT_ID, D.DEPARTMENT_NAME FROM HR.EMPLOYEES E JOIN HR.DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID WHERE E.DEPARTMENT_ID IS NOT NULL AND D.DEPARTMENT_NAME IS NOT NULL;"
      },
      {
        "path": "migration/oracle/data/002_select_employee.sql",
        "group": "data_extraction",
        "index": 1,
        "statement": "SELECT EMPLOYEE_ID, FIRST_NAME || ' ' || LAST_NAME AS EMPLOYEE_NAME, DEPARTMENT_ID FROM HR.EMPLOYEES;"
      },
      {
        "path": "migration/postgres/dml/003_insert_departments.sql",
        "group": "data_management",
        "index": 0,
        "statement": "INSERT INTO public.departments (department_id, department_name) VALUES {VALUES_PLACEHOLDER};"
      },
      {
        "path": "migration/postgres/dml/004_insert_employees.sql",
        "group": "data_management",
        "index": 1,
        "statement": "INSERT INTO public.employees (employee_id, employee_name, department_id) VALUES {VALUES_PLACEHOLDER};"
      }
    ],
    "placeholder": "{VALUES_PLACEHOLDER}",
    "summary": "Generated 2 Oracle to PostgreSQL table migration pairs."
  },
  "layout": {
    "extraction": "migration/oracle/data",
    "management": "migration/postgres/dml",
    "manifest": "migration/manifest.json"
  }
}