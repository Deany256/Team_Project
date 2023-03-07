import sqlite3

# Define the database file name
DATABASE = "Basic_DB.db"

# Define the function to create the Products table
def create_products_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                description TEXT,
                price REAL,
                image_url TEXT
            );
        """)

# Define the function to create the Customers table
def create_customers_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                shipping_address TEXT,
                payment_info TEXT
            );
        """)
        
# Define the function to create the Reviews table
def create_reviews_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Reviews (
                review_id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                rating INTEGER,
                text TEXT,
                FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                FOREIGN KEY (product_id) REFERENCES Products (product_id)
            );
        """)
        
create_customers_table()
create_products_table()
create_reviews_table()
